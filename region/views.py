from django.shortcuts import render
from .models import Country, Region


# Create your views here.

def country_list(request):
    countries = Country.objects.all()
    return render(request, '', {'country': countries})


def region_list(request):
    regions = Region.objects.all()
    return render(request, '', {'region': regions})
