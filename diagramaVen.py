import math
universo = int(input("Ingrese el Universo: "))
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
p = int(input("Ingrese 1Circulo: "))
q = int(input("Ingrese 2Circulo: "))
r = int(input("Ingrese 3Circulo: "))

print("_____a+x= {}".format(a))
print("_____b+x= {}".format(b))
print("_____c+x= {}".format(c))
s1 = a+b+c
print("a+b+c+3x= {}".format(s1))

print("a+c+p+x= {}".format(p))
print("a+b+q+x= {}".format(q))
print("c+b+r+x= {}".format(r))
s2 = p+q+r
print("2(a+b+c)+p+q+r+3x= {}".format(s2))

print("2(a+b+c)+p+q+r+3x= {}".format(s2))
print("---------a+b+c+3x= {}".format(s1))
s3 = s2-s1
print("______a+b+c+p+q+r= {}".format(s3))

print("____a+b+c+p+q+r+x= {}".format(universo))
print("____________{}+x= {}".format(s3,universo))
print("__________x= {} - {} = {}".format(universo,s3,(universo-s3)))