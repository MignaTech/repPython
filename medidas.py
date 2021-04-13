import math
def main():
        lista = Capturar()
        Ordenar(lista)
        rango = Rango(lista)
        media = Media(lista)
        mediana = Mediana(lista)
        modas = Moda(lista)
        desvi = Desviacion(lista, media)
        var = Varianza(desvi)
        Desplegar(lista, rango, media, mediana, modas, var, desvi)

def Capturar():
        lista = []
        n = int(input("\nIngrese la cantidad de datos: "))
        for x in range(1, n+1):
                print("Ingrese el", x, "valor", end=" ");num = float(input())
                lista.append(num)
        return lista

def Ordenar(lista):
        for x in range(1, len(lista)):
                for y in range(len(lista) - x):
                        if lista[y] > lista[y + 1]:
                                temp = lista[y]
                                lista[y] = lista[y + 1]
                                lista[y + 1] = temp

def Rango(lista):
        return (max(lista)+min(lista))/2

def Media(lista):
        return sum(lista)/len(lista)

def Desviacion(lista, media):
        aux = 0.0
        for x in lista:
                aux += (x-media)**2
        desvi = math.sqrt(aux/(len(lista)-1))
        return desvi

def Varianza(desvi):
        return pow(desvi, 2)

def Mediana(lista):
        n=len(lista)
        if(n % 2) > 0:
                mediana = lista[int(n/2)]
        else:
                mediana = (lista[int(n/2)-1]+lista[int(n/2)])/2
        return mediana

def Moda(lista):
        rep = 0
        for x in lista:
                num = lista.count(x)
                if num > rep:
                        rep = num
        modas = []
        for x in lista:
                num = lista.count(x)
                if num == rep and x not in modas:
                        modas.append(x)
        if (modas==lista):
                return "Amodal"
        else:
                return modas

def Desplegar(lista, rango, media, mediana, modas, var, desvi):
        for x in range(1, len(lista)+1):
                print("pos[",x,"] =",lista[x-1])
        print("Rango ========", format(rango, '7.2f'))
        print("Media ========", format(media, '7.4f'))
        print("Mediana ======", format(mediana, '7.4f'))
        print("Moda =========", format(modas))
        print("Varianza =====", format(var, '7.4f'))
        print("Desviacion ===", format(desvi, '7.4f'))

continuar = 's'
while continuar == 's' or continuar == 'S':
        main()
        continuar = input("Desea continuar (s/n):")
