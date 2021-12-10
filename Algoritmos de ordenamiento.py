import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random 

#creo el largo de las listas (de 100 a 10millones)
x=[]
def diferentes_largos():
    incremento=100
    for _ in range(11):
        x.append(incremento)
        incremento*= 4
    return x

print(diferentes_largos())
#funcion para medir tiempos

def tomarTiempos(x,funcion):
    execution_time = []
    results=[]
    for length in x:
        tiempo=0
        for i in range(1,6):
            np.random.seed(i)##np.random me genera las mismas listas
            list = np.random.randint(0, 100,size=length)
            start_time = time.time()
            results.append(funcion(list))
            end_time = time.time()
            print("Duration:",end_time - start_time, "s.")
            tiempo+=(end_time - start_time)
        tiempo/=5
        execution_time.append(tiempo)
    return execution_time


# Funcion 1.


a=[2,5,4,3,8,12,6]
def maxPos1(a):
    actual=len(a)-1    
    i=0
    grande=0
    while i <= actual:
        if(grande <= a[i]):
            grande=a[i]
            pos_max=i
        i+=1
    return pos_max
#print(maxPos1(a))

def upSortSlices(a):
    if len(a)==1:
        return a
    else:
        m=maxPos1(a)
        a[m],a[len(a)-1]=a[len(a)-1],a[m]
        return upSortSlices(a[:len(a)-1]) + [a[len(a)-1]]
print(upSortSlices(a))
print(a)


# Funcion 2
a=[2,5,4,3,8,12,6]

def maxPos2(a,actual):#actual=len(a)-1
    i=0
    grande=0
    while i <= actual:
        if(grande <= a[i]):
            grande=a[i]
            pos_max=i
        i+=1
    return pos_max

print(maxPos2(a, len(a)-1))
           
def upSortIndex(a):
    actual= len(a)-1
    while actual > 0:
        m= maxPos2(a,actual)
        a[m],a[actual]=a[actual],a[m]
        actual-=1
    return a

print(upSortIndex(a))

# Funcion 3

a=[1,2,5,14,4,7]

def bubbleSort(a):
    for _ in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(bubbleSort(a))


# Funcion 4

a=[1,4,5,3,6,4,2,8]
def mergeSortSlices(a):
    if len(a) > 1:
        mitad = len(a)//2
        inferior = a[:mitad ]
        superior = a[mitad :]
        mergeSortSlices(inferior)
        mergeSortSlices(superior ) 
        b=0#recorro inferior
        c=0#recorro superior
        d=0#voy poniendo en a 
        while b < len(inferior) and c < len(superior ):
            if inferior[b] < superior [c]:
                a[d] = inferior[b]
                b+= 1
            else:
                a[d] = superior [c]
                c+= 1
            d+= 1
        while b < len(inferior):
            a[d] = inferior[b]
            b+= 1
            d+= 1
        while c < len(superior ):
            a[d] = superior [c]
            c+= 1
            d+= 1
        return a
print(mergeSortSlices(a))


# Funcion 5

a=[4,1,3,2,9,8,2]

def mergeSortIndex(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: la lista ordenada."""
    return merge_sort_aux(lista, 0, len(lista)-1)

def merge_sort_aux(lista, i, j):
    """
    Ordena el segmento de la lista que va
    desde el índice i hasta el j (inclusive).
    Lo hace "inplace".
    """
    if j - i == 1:
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]   
    elif j - i >= 2:
        medio = (i + j) // 2
        lista = merge_sort_aux(lista, i, medio-1)
        lista = merge_sort_aux(lista, medio, j)
        lista = merge(lista, i, medio, j)
    return lista

def merge(lista, inicial, mitad, final):
    """
    Hace un merge entre dos segmentos de la lista:
    1) desde el índice inicial hasta mitad-1
    2) desde mitad hasta final (inclusive)
    """
    lista_nueva = []
    i = inicial
    orig_empieza=i
    j = mitad
    while i < mitad and j <= final:   
        if lista[i] <= lista[j]:    
            lista_nueva.append(lista[i])
            i += 1
        else:
            lista_nueva.append(lista[j])
            j += 1
    while i < mitad:  #Modifique un poco la funcion por que me tiraba este error
        lista_nueva.append(lista[i])# con tomar tiempo. ValueError: operands could not be broadcast together with shapes (2,) (3,) 
        i+=1
    while j <= final:
        lista_nueva.append(lista[j])
        j+=1
    for h in lista_nueva:
        lista[orig_empieza] = h
        orig_empieza += 1
    return lista

print(mergeSortIndex(a))

# Funcion 6 

a=[5,2,8,3,6,4,3]

def particion(a):
    pivot = a[0]
    menores=[]
    mayores=[]
    for i in range(1,len(a)):
        if a[i] < pivot:
            menores.append(a[i])
        else:
            mayores.append(a[i])
    return menores, pivot, mayores
    
def quickSortCopy(a):
    if len(a)< 2:
        return a
    else:
        menores,pivot,mayores=particion(a)
    return quickSortCopy(menores) + [pivot] + quickSortCopy(mayores)
    
print(quickSortCopy(a))

#7)

a=[5,2,8,3,6,4,3]

def particion2(a,menor,mayor):
    pivot = a[menor]
    izq=menor+1
    der=mayor
    while True: 
        while a[izq]<pivot and izq < der:
            izq+=1
        while a[der]>=pivot and izq <= der:
            der-=1
        if izq >= der:
            break
        else:
            a[izq],a[der]=a[der],a[izq]
    #itercambiar el pivot con der
    a[menor],a[der]=a[der],a[menor]
    return der


def QuicksortIndex(a ,low, high):
    if (low < high):
        pivotPosicion=particion2(a,low,high)
        QuicksortIndex(a,low,pivotPosicion-1)
        QuicksortIndex(a,pivotPosicion+1,high)
    return a

# funcion con un solo parametro para poder usar tomarTiempos
def quickSortIndex(a):
    return QuicksortIndex(a, 0, len(a)-1)

print(a)

quickSortIndex(a)

print(a)

def n_2(x):
    tiempo_teo_n=[]
    for i in x:
        n_2=((i)**2)*0.000001
        tiempo_teo_n.append(n_2)
    return tiempo_teo_n

print(n_2(x))

def n_logn(x):
    tiempo_teo_log=[]
    for i in x:
        n_log=(i)*np.log10(i)*0.00005
        tiempo_teo_log.append(n_log)
    return tiempo_teo_log
print(n_logn(x))

### Medicion de tiempos

tiempo_1= tomarTiempos(x,upSortSlices) 
tiempo_2= tomarTiempos(x,upSortIndex)
tiempo_3= tomarTiempos(x,bubbleSort)
tiempo_4= tomarTiempos(x,mergeSortSlices)
tiempo_5= tomarTiempos(x,mergeSortIndex)
tiempo_6= tomarTiempos(x,quickSortCopy)
tiempo_7= tomarTiempos(x,quickSortIndex)
tiempo_8= tomarTiempos(x,sorted) 
tiempo_teo_n= n_2(x)
tiempo_teo_log= n_logn(x)


datos1=pd.DataFrame(zip(x,tiempo_1),columns=("largo de la lista","Tiempo de ejecucion"))
datos2=pd.DataFrame(zip(x,tiempo_2),columns=("largo de la lista","Tiempo de ejecucion"))
datos3=pd.DataFrame(zip(x,tiempo_3),columns=("largo de la lista","Tiempo de ejecucion"))
datos4=pd.DataFrame(zip(x,tiempo_4),columns=("largo de la lista","Tiempo de ejecucion"))
datos5=pd.DataFrame(zip(x,tiempo_5),columns=("largo de la lista","Tiempo de ejecucion"))
datos6=pd.DataFrame(zip(x,tiempo_6),columns=("largo de la lista","Tiempo de ejecucion"))
datos7=pd.DataFrame(zip(x,tiempo_7),columns=("largo de la lista","Tiempo de ejecucion"))
datos8=pd.DataFrame(zip(x,tiempo_8),columns=("largo de la lista","Tiempo de ejecucion"))
datos9=pd.DataFrame(zip(x,tiempo_teo_n),columns=("largo de la lista","Tiempo de ejecucion"))
datos10=pd.DataFrame(zip(x,tiempo_teo_log),columns=("largo de la lista","Tiempo de ejecucion"))

### Grafico

fig, ax=plt.subplots()
ax.plot(datos2["largo de la lista"],
        datos2["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="blue",
        alpha=1)
ax.plot(datos3["largo de la lista"],
        datos3["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="green",
        alpha=1)
ax.plot(datos9["largo de la lista"],
        datos9["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="black",
        alpha=0.7)
ax.legend(['upSortIndex()',"bubbleSort()","O(n^2)"])
ax.set_xlabel("Largo de la lista")
ax.set_ylabel("Tiempo de ejecucion(s)")
ax.set_title("Tiempos de ejecucion de los distintos algoritmos")
plt.savefig("grafico tiempos n^2.pdf")
plt.show()



fig, ax=plt.subplots()
ax.plot(datos4["largo de la lista"],
        datos4["Tiempo de ejecucion"],
        marker="o",
        color="red",
        alpha=1)
ax.plot(datos5["largo de la lista"],
        datos5["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="orange",
        alpha=1)
ax.plot(datos6["largo de la lista"],
        datos6["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="m",
        alpha=0.7)
ax.plot(datos7["largo de la lista"],
        datos7["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="yellow",
        alpha=0.7)
ax.plot(datos8["largo de la lista"],
        datos8["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="maroon",
        alpha=0.7)
ax.plot(datos10["largo de la lista"],
        datos10["Tiempo de ejecucion"],
        marker="o",
        linestyle="--",
        color="black",
        alpha=0.7)
ax.legend(['mergeSortSlices()',"mergeSortIndex()","quickSortCopy()","quickSortIndex()","sorted()","O(n log(n))"])
ax.set_xlabel("Largo de la lista")
ax.set_ylabel("Tiempo de ejecucion(s)")
ax.set_title("Tiempos de ejecucion de los distintos algoritmos")
plt.savefig("grafico tiempos n log(n).pdf")
plt.show()



