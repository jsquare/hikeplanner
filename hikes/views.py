from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from hikes.models import Hike
from django.shortcuts import render_to_response, render
from django.contrib.gis import forms
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from urllib import urlencode
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr, Point
from django.template import RequestContext
from django.core.context_processors import csrf

# Create your views here.

class SearchForm(forms.Form):
    start_location =  forms.CharField()
    start_latitude = forms.FloatField(widget=forms.HiddenInput())
    start_longitude = forms.FloatField(widget=forms.HiddenInput())
    min_radius = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    max_radius = forms.IntegerField(widget=forms.HiddenInput(),initial=1)
    min_length = forms.IntegerField(widget=forms.HiddenInput(),initial=1)
    max_length = forms.IntegerField(widget=forms.HiddenInput(),initial=2)
    min_terrain = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    max_terrain = forms.IntegerField(widget=forms.HiddenInput(), initial=1)

def home(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:  
        form = SearchForm()

    context = {
        'form' : form
    }

    return render_to_response('search.html', context_instance = RequestContext(request))

def results(request):
    form = SearchForm(request.GET)

    if not form.is_valid():
        url = reverse('home')
        params = urlencode(request.GET)
        return HttpResponseRedirect('%s?%s' % (url,params))

    # Request hikes from db within min and max day limits
    min_days = form.cleaned_data['min_length']  # TODO: change db fields to be min/max length instead of days. TODO: convert 'lengths' ==> days
    max_days = form.cleaned_data['max_length']
    radius = form.cleaned_data['max_radius']    # TODO: support min radius
    start_latitude = form.cleaned_data['start_latitude']
    start_longitude = form.cleaned_data['start_longitude']

    start_location = Point(start_longitude,start_latitude)

    hike_list = Hike.objects.filter(days__gte=min_days, days__lte=max_days,location__distance_lt=(start_location, D(km=radius)))
    
    context = {
        'hike_list' : hike_list,
        'page_title' : 'Hike Results'
    }

    hike_str = "Here are all the hikes within your limits: {}".format([hike.__unicode__() for hike in hike_list])
    
    return render_to_response('results.html', context)

def hike_detail(request, hike_id, slug=''):
    '''
    The general information page about a hike.
    @param slug: optional, ignored (allows StackOverflow-style URL)
    '''
    try:
        hike = Hike.objects.get(id=hike_id)
    except Hike.DoesNotExist:
        return HttpResponseNotFound() # TODO

    context = {
        'hike': hike,
        'page_title': hike.name,
    }
    return render_to_response('hike_detail.html', context)

#Gets called when a user submits login info. Authenticates and redirects user.
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        #Verified corect password, user is marked as active, so log them in
        auth.login(request, user)
        #Redirect to success page
        return HttpResponseRedirect("/account/loggedin")
    else:
        #Show error page
        return HttpResponseRedirect("/account/invalid")

#Gets called when user clicks on logout
def logout(request):
    auth.logout(request)
    #REdirect to success page
    return HttpResponseRedirect("/")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = UserCreationForm()
        return render_to_response('register.html', args)    

