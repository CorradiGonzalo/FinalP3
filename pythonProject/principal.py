from registro import *
import random

def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    while num < inf:
        print("El numero debe ser mayor a ", inf)
        num = int(input(mensaje))
    return num


def cargar_vector(v):
    for i in range(len(v)):
        nombre = 'Pais ' + str(i)
        continente = random.randint(0, 4)
        oro = random.randint(0,50)
        plata = random.randint(0, 50)
        bronce = random.randint(0, 50)
        v[i] = Pais(nombre, continente, oro, plata, bronce)


def mostrar_menu():
    print("1-")
    print("2-")
    print("3-")
    print("4-")
    print("5-")
    print("0-Salir")
    op = int(input("Ingrese una opcion: "))
    return op


def ordenar_vector(v):
    #Seleccion directa
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].total < v[j].total:
                v[i], v[j] = v[j], v[i]


def mostrar_listado(v):
    """Listado ordenado de medallas de mayor a menor"""
    ordenar_vector(v)
    for i in range(len(v)):
        print(v[i])


def validar_entre(inf, sup, mensaje):
    continente = int(input(mensaje))
    while continente < inf or continente > sup:
        print("Error")
        continente = int(input(mensaje))
    return continente


def calcular_promedio(suma, cant):
    prom = 0
    if cant != 0:
        prom = suma / cant
    return prom


def promediar_oro(v, continente):
    suma, cant = 0, 0
    for i in range(len(v)):
        suma += v[i].oro
        cant += 1
    return calcular_promedio(suma, cant)


def mayor_plata(v):
    may = v[0]
    for i in range(1, len(v)):
        if v[i].plata > may:
            may = v[i]
    return may


def solo_bronce(v):
    cant = 0
    for i in range(len(v)):
        if v[i].oro == 0 and v[i].plata == 0 and v[i].bronce > 0:
            cant += 1
    return cant


def prom_bronce(cant, v):
    prom = 0
    if cant != 0:
        prom = cant / len(v)
    return prom


def porc_bronce(cant, v):
    porc = 0
    if cant != 0:
        porc = cant * 100 / len(v)
    return porc


def contar_por_continente(v):
    cont = [0] * 5
    for pais in v:
        cont[pais.continente] += 1
    return cont


def mostrar_conteo(cont):
    for i in range(len(cont)):
        print("Continente ", i, ":", cont[i], " paises.")


def principal():
    print("MEDALLERO OLIMPICO")
    n = validar_mayor_que(0, 'Ingrese cantidad de paises:')
    v = [None] * n
    cargar_vector(v)
    opcion = -1
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            mostrar_listado(v)
        elif opcion == 2:
            continente = validar_entre(0, 4, 'Ingrese Continente:')
            promedio = promediar_oro(v, continente)
            print("El promedio es: ", promedio)
        elif opcion == 3:
            may = mayor_plata(v)
            print("El pais con la mayo cantidad de medallas de plata es: ", may)
        elif opcion == 4:
            cant = solo_bronce(v)
            porc = porc_bronce(cant, v)
            print("El promedio es: ", porc)
        elif opcion == 5:
            cont = contar_por_continente(v)
            mostrar_conteo(cont)
        elif opcion == 0:
            print("Gracias...")
        else:
            print("Opcion incorrecta")
