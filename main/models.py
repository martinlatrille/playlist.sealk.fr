#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class TypePlaylist(models.Model):
	type = models.CharField(max_length=64)
	date = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.type
		
	def __str__(self):
		return self.type
		
class Song(models.Model):
	type = models.ForeignKey('TypePlaylist')
	name = models.CharField(max_length=128)
	artist = models.CharField(max_length=256)
	date = models.DateTimeField(auto_now_add=True)
	adress = models.CharField(max_length=32)
	
	def __unicode__(self):
		return self.artist + " - " + self.name
		
	def __str__(self):
		return self.artist + " - " + self.name