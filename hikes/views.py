from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from hikes.models import Hike
from django.shortcuts import render_to_response
from django.contrib.gis import forms
from django.core.urlresolvers import reverse
from urllib import urlencode
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr, Point

# Create your views here.

class SearchForm(forms.Form):
    start_location =  forms.CharField()
    start_latitude = forms.FloatField(widget=forms.HiddenInput())
    start_longitude = forms.FloatField(widget=forms.HiddenInput())
    radius = forms.IntegerField()
    min_days = forms.IntegerField()
    max_days = forms.IntegerField()

def home(request):
    if request.GET:
        form = SearchForm(request.GET)
    else:  
        form = SearchForm()

    context = {
        'form' : form
    }

    return render_to_response('search.html', context)

def results(request):
    form = SearchForm(request.GET)

    if not form.is_valid():
        url = reverse('home')
        params = urlencode(request.GET)
        return HttpResponseRedirect('%s?%s' % (url,params))

    # Request hikes from db within min and max day limits
    min_days = form.cleaned_data['min_days']
    max_days = form.cleaned_data['max_days']
    radius = form.cleaned_data['radius']
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


