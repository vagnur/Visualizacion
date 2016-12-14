from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'bnbg/index.html')
def tendencias(request):
	return render(request, 'bnbg/tendencias.html')
def burbujas(request):
	return render(request,'bnbg/burbujas.html')
def arbol(request):
	return render(request,'bnbg/arbol.html')