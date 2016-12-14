from django.conf.urls import patterns, url
from bnbg import views

urlpatterns = patterns('bnbg.views',
	url(r'^$', 'index', name='index'), 
	url(r'^index/', views.index,name='index'),
	url(r'^tendencias/',views.tendencias,name='tendencias'),
	url(r'^burbujas/',views.burbujas,name='burbujas'),
	url(r'^arbol/',views.arbol,name='arbol'),
)