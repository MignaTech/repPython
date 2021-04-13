import math
def ecua(x):
	e=-0.5*pow(x,2)+2.5*x+4.5
  return e
def escribir(men):
	print(men)
def ci(men):
	escribir(men);xx=int(input());return xx
def cf(men):
	escribir(men);xx=float(input());return xx

escribir("programa para el metodo de biseccion")
xi=ci("Inicio: ")
xf=ci("final:")
p=cf("factor de error ejemplo 0.001:")
fac=p/100
xr = 0
while True:
	ant = xr
	xr = (xi+xf)/2
	fxi = ecua(xi)
	fxr = ecua(xr)
	f=((xi+xr)/2)-xi
	if(fxi*fxr < 0):
		xf = xr
	else:
		xi = xr
	print("{:14.12f} ==> {:14.12f}".format(xr,ecua(xr)))#format(xr,f))
	if f < fac:
		xr = ant
		break
