from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Card

def index(request):
    cards = Card.objects.order_by('name')
    template = loader.get_template('cards/index.html')
    context = {
        'cards': cards,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    card = Card.objects.filter(number = id)[0]
    template = loader.get_template('cards/detail.html')
    context = {
        'card': card,
    }
    return HttpResponse(template.render(context, request))
