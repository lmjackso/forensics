from django.conf.urls import patterns, include, url
from django.contrib.auth.views import *

urlpatterns = patterns('',

	url(r'^$', 'DFA.views.home', name='home'),
	url(r'^home$', 'DFA.views.home', name='home'),

	url(r'^export$', 'DFA.views.export', name='export'),

	url(r'^single$', 'DFA.views.single', name='single'),
	url(r'^comparison$', 'DFA.views.comparison', name='comparison'),
)