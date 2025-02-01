import json
from django.shortcuts import render
from .models import NavItem, Formulation
from django.http import HttpResponse
from .form import CreateFormulation
from django.http import JsonResponse
from user_agents import parse

def divace(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    format_response = parse(user_agent)

    return {
        'is_mobile': format_response.is_mobile,
        'is_tablet': format_response.is_tablet,
        'is_pc': format_response.is_pc,
    }

def Home(request):
    Item = NavItem.objects.all()
    data = divace(request)
    movil = False
    
    if data['is_mobile'] or data['is_tablet']:
        movil = True
     
        
    return render(request, 'templetes/index.html', {'menu_items': Item, 'menu_movil': movil})


def About(request):
    return render(request,'templetes/about.html')


def Contact(request):
    forms = Formulation.objects.all()
    if request.method == "POST":
        form = CreateFormulation(request.POST)
        
        if form.is_valid():
            return HttpResponse("Data seccess")
        
        else:
          return render(request,'templetes/contact.html', {'message:': forms})
