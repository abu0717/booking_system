from django.shortcuts import render
from .models import Country, Region
from rent_house.models import RentHouse


# Create your views here.

def country_list(request):
    countries = Country.objects.all()
    return render(request, '', {'country': countries})


def region_list(request):
    regions = Region.objects.all()
    return render(request, '', {'region': regions})


def detail_country(request, pk):
    rent_house = RentHouse.objects.filter(country__id=pk)
    return render(request, '', {'rent_house': rent_house})
