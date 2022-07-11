from django.shortcuts import render
from .models import Charity, Volnteer

def choose_volnteer_charity(request):
    return render(request, 'volnteerandcharity/volnteercharity.html')


def volnteer(request):
    volnteer_list = Volnteer.objects.all()
    return render(request, 'volnteerandcharity/volnteers.html', {'volnteer_list':volnteer_list})


def charities(request):
    charities_list = Charity.objects.all()
    return render(request, 'volnteerandcharity/charities.html', {'charities_list':charities_list})

def filter_volnteer_child(request):
    volnteer_list = Volnteer.objects.filter(type = 'children')
    return render(request, 'volnteerandcharity/vol_child.html', {'volnteer_list':volnteer_list})

def filter_volnteer_singleparent(request):
    volnteer_list = Volnteer.objects.filter(type = 'single parent')
    return render(request, 'volnteerandcharity/vol_singleparent.html', {'volnteer_list':volnteer_list})

def filter_volnteer_elders(request):
    volnteer_list = Volnteer.objects.filter(type = 'elders')
    return render(request, 'volnteerandcharity/vol_singleparent.html', {'volnteer_list':volnteer_list})


def filter_charity_child(request):
    charities_list = Charity.objects.filter(type = 'children')
    return render(request, 'volnteerandcharity/char_child.html', {'charities_list':charities_list})

def filter_charity_singleparent(request):
    charities_list = Charity.objects.filter(type = 'single parent')
    return render(request, 'volnteerandcharity/char_singleparent.html', {'charities_list':charities_list})

def filter_charity_elders(request):
    charities_list = Charity.objects.filter(type = 'elders')
    return render(request, 'volnteerandcharity/char_elders.html', {'charities_list':charities_list})
