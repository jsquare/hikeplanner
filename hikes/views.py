from django.http import HttpResponse, HttpResponseRedirect
from hikes.models import Hike
from django.shortcuts import render_to_response
from django import forms
from django.core.urlresolvers import reverse
from urllib import urlencode

# Create your views here.

class SearchForm(forms.Form):
    min_days = forms.IntegerField()
    max_days = forms.IntegerField()

def home(request):
    hike_list = Hike.objects.all()

    hike_str = "Here are all the hikes: {}".format([hike.__unicode__() for hike in hike_list])

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

    hike_list = Hike.objects.filter(days__gte=min_days, days__lte=max_days)
    
    context = {
        'hike_list' : hike_list
    }

    hike_str = "Here are all the hikes within your limits: {}".format([hike.__unicode__() for hike in hike_list])
    
    return render_to_response('results.html', context)




