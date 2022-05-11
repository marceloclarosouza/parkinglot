from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Wellcome to the Ace Parking Lot")

def feedback(request):

    return HttpResponse("Feedback page")

