from django.shortcuts import render
from django.http import HttpResponse
import random as rd

def index(request):
	return render(request,'bnbg/index.html')
def tendencias(request):
	return render(request, 'bnbg/tendencias.html')
def burbujas(request):
	return render(request,'bnbg/burbujas.html')
def burbujas2(request):
	return render(request,'bnbg/burbujas2.html')
def burbujas3(request):
	return render(request,'bnbg/burbujas3.html')
def burbujas4(request):
	return render(request,'bnbg/burbujas4.html')
def arbol(request):
	data = open('juegos.csv','r')
	return render(request,'bnbg/arbol.html',{'data':data})
def selectGame(request):
	game = str(request.POST.get('dato'))
	
	borrar = open('bnbg/static/bnbg/datos/flare2.json','w')
	borrar.close()

	juego = game.strip()

	print juego

	datos = open('bnbg/static/bnbg/datos/datos','r')

	cat = []
	mec = []
	jue = []
	usados = []

	for dato in datos:
		dato = dato.strip().split(',')
		nombre = dato[5].split('+')
		categorias = dato[6].split('|#|')
		mecanicas = dato[7].split('|#|')
		if nombre[0] == juego:
			for categoria in categorias:
				cat.append(categoria)
			for mecanica in mecanicas:
				mec.append(mecanica)			

	for categoria in cat:
		ctg = []
		for mecaninca in mec:
			mcn = []
			datos.seek(0,0)
			contador = 0
			for dato in datos:
				dato = dato.strip().split(',')
				jueg = dato[5]
				jueg = jueg.split('+')
				cate = dato[6].split('|#|')
				meca = dato[7].split('|#|')
				for cattt in cate:
					if cattt == categoria:
						for mcnnn in meca:
							if mcnnn == mecanica and contador<5 and jueg[0]!=juego:
								mcn.append(jueg[0])
								contador+=1
			ctg.append(mcn)
		if len(ctg)>0:
			jue.append(ctg)

	with open('bnbg/static/bnbg/datos/flare2.json','a') as salida:
		salida.write('{'+'\n')
		salida.write('"name": "'+juego+'",'+'\n')
	  	salida.write('"children": ['+'\n')

	for j in range(0,len(cat)):	
		if j==0:
			linea = '{\n'+'"name": "Categoria: '+cat[j]+'",\n"children": [\n'
		else:
			linea = ',{\n'+'"name": "Categoria: '+cat[j]+'",\n"children": [\n'
		for i in range(0,len(mec)):
			if i==0:
				linea = linea + '{\n'+'"name": "Mecanica: '+mec[i]+'",\n"children": [\n'
			else:
				linea = linea + ',{\n'+'"name": "Mecanica: '+mec[i]+'",\n"children": [\n'
			for l in range(0,len(jue[j][i])):
				if l!=4:
					linea = linea + '{"name": "'+jue[j][i][l].encode('utf8','ignore')+'", "size": '+str(rd.randint(1,3)**l+1)+'},\n'	
				else:
					linea = linea + '{"name": "'+jue[j][i][l].encode('utf8','ignore')+'", "size": '+str(rd.randint(1,3)**l+1)+'}\n]}'
			if i==len(mec)-1:
				linea = linea + ']}'

		with open('bnbg/static/bnbg/datos/flare2.json','a') as salida:
			salida.write(linea+'\n')

	with open('bnbg/static/bnbg/datos/flare2.json','a') as salida:
		salida.write(']}'+'\n')
	return render(request,'bnbg/selectGame.html',{'game':game})