import random

def llenarlista(tamaño,rango):
    tam=random.randint(15,tamaño)
    lista=[round(random.uniform(1.50,rango),2) for i in range(tam)]
    return lista

lista1=llenarlista(125,2.00)

def ascendente(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    return lista

print(ascendente(lista1))

l1=llenarlista(125,2.00)
saltoq=len(l1)/5

def quintil(lista):
    quintil=0
    while not quintil==len(l1):
        q1=quintil+saltoq
        print("El primer quintil va de ",quintil+1, "Hasta ",q1)
        q2=q1+saltoq
        print("El segundo quintil va de ",q1+1, "Hasta ",q2)
        q3=q2+saltoq
        print("El tercer quintil va de ",q2+1, "Hasta ",q3)
        q4=q3+saltoq
        print("El cuarto quintil va de ",q3+1, "Hasta ",q4)
        q5=q4+saltoq
        print("El quinto quintil va de ",q4+1, "Hasta ",q5)
        quintil==q5
        break

print(quintil(l1))

l2=llenarlista(125,2.00)
saltoc=len(l2)/4
def cuartil(lista):
    cuartil=0
    while not cuartil==len(l1):
        c1=cuartil+saltoc
        print("El primer cuartil va de ",cuartil+1, "Hasta ",c1)
        c2=c1+saltoc
        print("El segundo cuartil va de ",c1+1, "Hasta ",c2)
        c3=c2+saltoc
        print("El tercer cuartil va de ",c2+1, "Hasta ",c3)
        c4=c3+saltoc
        print("El cuarto cuartil va de ",c3+1, "Hasta ",c4)
        c5=c4+saltoc
        print("El quinto cuartil va de ",c4+1, "Hasta ",c5)
        cuartil==c5
        break

print(cuartil(l2))





