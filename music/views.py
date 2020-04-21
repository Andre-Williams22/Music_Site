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

def album_detail(request, album_id):
    album_details = Album.objects.get(id=album_id)
    context = {'album_details': album_details,
                'id': album_id}
    return render(request, 'adetails.html', context)

def song_detail(request, song_id):
    song_details = Song.objects.get(id=song_id)
    context = {'song_details': song_details,
                'id':song_id}
    render(request, 'sdetails.html', context)

# class AlbumDetailView(generic.DetailView):
#     model = Album
#     template = 'views/adetails.html'

# class SongDetailView(generic.DetailView):
#     model = Song
#     template = 'views/sdetails.html'

# class ResultsView(generic.DetailView):
#     model = Musician
#     template = 'views/results.html'    
    
