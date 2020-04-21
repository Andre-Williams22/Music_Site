from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse 
from django.views import generic 


#import models 
from .models import *

# Create your views here.

def about(request):
    context = {
        'favorite_color': 'blue'
    }

    return render(request, 'music/about.html', context)

def index_view(request):
    ''' Return the last five musicians '''
    latest_musicians = Musician.objects.order_by('-pub_date')[:5]
    context = {'latest_musicians': latest_musicians}
    return render(request, 'music/index.html', context)

def musician_detail(request, musician_id):
    musician_details = Musician.objects.get(id=musician_id)
    context = {'musician_details': musician_details,
                'id': musician_id}

    return render(request, 'music/mdetails.html', context)


# class AlbumDetailView(generic.DetailView):
#     model = Album
#     template = 'views/adetails.html'

# class SongDetailView(generic.DetailView):
#     model = Song
#     template = 'views/sdetails.html'

# class ResultsView(generic.DetailView):
#     model = Musician
#     template = 'views/results.html'    
    
