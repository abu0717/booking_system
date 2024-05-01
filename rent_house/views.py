from django.shortcuts import render
from .models import RentHouse
from django.core.paginator import Paginator


# Create your views here.

def post_house(request):
    if request.method == 'POST':
        name = request.POST('name')
        type = request.POST('type')
        description = request.POST('description')
        neighboorhood = request.POST('neighboorhood')
        location = request.POST('location')
        policy = request.POST('policy')
        price = request.POST('price')
        rent_house = RentHouse(name=name, type=type, description=description, neighboorhood=neighboorhood,
                               location=location,
                               policy=policy, price=price, user=request.user)
        rent_house.save()


def get_house(request):
    houses = RentHouse.objects.all()
    p = Paginator(houses, 50)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, '', {
        'houses': houses,
        'page_obj': page_obj
    })


def retrieve_house(request, pk):
    house = RentHouse.objects.filter(pk=pk)
    return render(request, '', context={'house': house})


def delete_house(request, pk):
    house = RentHouse.objects.filter(pk=pk)
    house.delete()
    return render(request, '')


def update_house(request, pk):
    house = RentHouse.objects.filter(pk=pk)
    if request.method == 'POST':
        house.name = request.POST('name')
        house.type = request.POST('type')
        house.description = request.POST('description')
        house.neighboorhood = request.POST('neighboorhood')
        house.location = request.POST('location')
        house.policy = request.POST('policy')
        house.price = request.POST('price')
        house.save()
