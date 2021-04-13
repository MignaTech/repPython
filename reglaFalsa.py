import math
def ecua(x):
	e=-.5*pow(x,2) +2.5*x +4.5
	return e
def mi(men):
	print(men,end="");entero=int(input());return entero
def mf(men):
	print(men,end="");flotante=float(input());return flotante

print ("Programa de regla falsa")
a = mi("Inicio: ");b = mi("Final: ")
fac = mf("Factor (ejemplo 0.01): ")
while True:
	fa = ecua(a);fb = ecua(b)
	c = ((fa*b) - (fb*a)) / (fa-fb)
	fc = ecua(c)
	print("{:20.18f} {:20.18f}".format(c,abs(fa*fc)))
	if (fa*fc) < 0:
		b=c
	else:
		a=c
	if (abs(fa*fc)<=fac): break
print(ecua(c))
