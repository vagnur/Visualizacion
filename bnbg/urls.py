from django.conf.urls import patterns, url
from bnbg import views

urlpatterns = patterns('bnbg.views',
	url(r'^$', 'index', name='index'), 
	url(r'^index/', views.index,name='index'),
	url(r'^tendencias/',views.tendencias,name='tendencias'),
	url(r'^burbujas/',views.burbujas,name='burbujas'),
	url(r'^burbujas2/',views.burbujas2,name='burbujas2'),
	url(r'^burbujas3/',views.burbujas3,name='burbujas3'),
	url(r'^burbujas4/',views.burbujas4,name='burbujas4'),
	url(r'^arbol/',views.arbol,name='arbol'),
	url(r'^selectGame/',views.selectGame,name='selectGame'),
)