from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Feedback, Service

def index(request):
    return HttpResponse("Wellcome to the Ace Parking Lot")

def get_feedback(request):
    feed = Feedback.objects.all()
    context = {'feed': feed}
    
    return render(request, 'services/feedback.html', context)

def get_services(request):
    service = Service.objects.all()
    context = {'service': service}
    
    return render(request, 'services/services.html', context)

