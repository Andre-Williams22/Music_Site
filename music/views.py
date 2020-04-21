from django.shortcuts import render
from django.http import HttpResponse 

#import models 
from .models import *

# Create your views here.

def about(request):
    context = {
        'favorite_color': 'blue'
    }

    return render(request, 'myapp/about.html', context)

