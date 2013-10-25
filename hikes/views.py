from django.http import HttpResponse
from hikes.models import Hike

# Create your views here.

def index(request):
    hike_list = Hike.objects.all()

    hike_str = "Here are all the hikes: {}".format([hike.__unicode__() for hike in hike_list])

    return HttpResponse(hike_str)
