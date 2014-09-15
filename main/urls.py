from django.conf.urls import url, patterns

urlpatterns = patterns('',
	url(r'^$', 'main.views.home'),
	url(r'^([A-Za-z]*)$', 'main.views.type'),
	url(r'^([A-Za-z]*)/Add$', 'main.views.addSong'),
	url(r'^([A-Za-z]+)/([a-zA-Z0-9_]+)$', 'main.views.typeSong'),
)
