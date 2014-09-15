#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from main.models import TypePlaylist, Song
from main.forms import AddSongForm

# Create your views here.

def home(request):
	types = TypePlaylist.objects.all()
	return render(request, 'main/index.html', {'types':types})
  
def type(request, type):
	types = TypePlaylist.objects.all()
	style = TypePlaylist.objects.get(type=type)
	songs = style.song_set.all()
	return render(request, 'main/type.html', locals())
	
def typeSong(request, type, song):
	types = TypePlaylist.objects.all()
	style = TypePlaylist.objects.get(type=type)
	songs = style.song_set.all()
	return render(request, 'main/type.html', locals())
	
def addSong(request, type):
	types = TypePlaylist.objects.all()
	
	if request.method == 'POST':
		form = AddSongForm(request.POST)
		hasWorked = False
		
		if form.is_valid():
			hasWorked = True
			name = form.cleaned_data['name']
			artist = form.cleaned_data['artist']
			adress = form.cleaned_data['adress']
			form.save()
			
	else:
		form = AddSongForm()
		
	return render(request, 'main/add.html', locals())