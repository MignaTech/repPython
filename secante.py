import math
def ecua(x):
	e=-.5*pow(x,2) +2.5*x +4.5
	return e
def mi(men):
	print(men,end="");entero=int(input());return entero
def mf(men):
	print(men,end="");flotante=float(input());return flotante
	
print ("Programa de secante")
a = mi("Inicio: ");b = mi("Final: ")
fac = mf("Factor: (ejemplo: 0.001): ")
fa = ecua(a);fb = ecua(b)
while True:
	c = b - (fb*((b-a) / (fb-fa)))
	f = abs((c-b)/c)
	fc = ecua(c)
	print("{:20.18f} {:20.18f}".format(c,f))
	a = b;b = c
	fa = fb;fb = fc
	if (abs(f)<fac and f==0):
		break
print(ecua(c))
