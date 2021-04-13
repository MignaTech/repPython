import os
ruta = "ejemplos.csv"
while True:
	print("MENÚ")
	print("1.- AGREGAR")
	print("2.- VER DATOS")
	print("3.- SALIR")
	opcion=input("SELECCIONA UNA OPCIÓN: ")
	os.system ("cls")
	if (opcion=="1"):
		print("DATOS")
		archivo = open(ruta,"a")
		matricula = input("MATRICULA: ")
		nombre = input("NOMBRE: ")
		telefono = input("TELEFONO: ")
		edad = input("EDAD: ")
		peso = input("PESO: ")
		archivo.write(matricula+",")
		archivo.write(nombre+",")
		archivo.write(telefono+",")
		archivo.write(edad+",")
		archivo.write(peso+"\n")
		archivo.close()
		input();os.system ("cls")
	elif (opcion == "2"):
		print("REGISTROS")
		archivo = open(ruta,"r")
		print(archivo.read())
		archivo.close()
		input();os.system ("cls")
	elif (opcion == "3"):
		print("ADIOS")
		input()
		break
	elif (opcion == "8"):
		archivo = open(ruta,"a")
		archivo.truncate()
		print("Registros eliminados")
		archivo.close()
	else:
		print("OPCIÓN NO VALIDA")
