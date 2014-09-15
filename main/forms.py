#-*- coding: utf-8 -*-
from django import forms
from main.models import Song

class AddSongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['type', 'name', 'artist', 'adress']
