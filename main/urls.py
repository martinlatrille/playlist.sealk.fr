from django.conf.urls import url, patterns

urlpatterns = patterns('',
	url(r'^$', 'main.views.home'),
	url(r'^([0-9A-Za-z]*)$', 'main.views.type'),
	url(r'^([0-9A-Za-z]*)/Add$', 'main.views.addSong'),
	url(r'^([0-9A-Za-z]+)/([a-zA-Z0-9_]+)$', 'main.views.typeSong'),
)
