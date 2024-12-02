# proyecto  RETO 1 - Proyecto de Investigación Científica en Python
# @author: MANUEL AURELIO BARRERA BOTIA Y MILLER ERNESTO RODRIGUEZ TINJACA

from datetime import datetime
from colorama import init, Fore, Back, Style
from colorama import Cursor, init, Fore
from prettytable import PrettyTable 
import statistics

#Lista para almacenar los experimentos
listaDeExperimentos = [
    ["Experimento 1","26/11/2024","Física", [5,6,2,7,8,9]],
    ["Experimento 2","27/11/2024","Quimica", [2,4,6,8,10,12]]
]

#Funcion para agregar un nuevo experimento
def agregar_experimento():
    
    nombre = input("Ingrese el nombre del experimento: ")
    fecha = input("Ingrese la fecha del experimento: DD/MM/YYYY ")
    tipo = input("Ingrese el tipo de expeimento (Quimica, Biologia, Fisica): ")
    
    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y") #Validar la fecha
        resultados = list(map(int, input("Ingrese los resultados numericos separados por comeas: ").split(",")))
        listaDeExperimentos.append([nombre,fecha,tipo,resultados])
        print("\033[1;32m"+"Experimentos agregados con exito"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

#Funcion para eliminar un experimento
def eliminar_experimento():
    visulizar_experimentos()
    
    try:
        indice = int(input("Ingrese el indice del experimento a eliminar: ")) - 1
        if 0 <= indice < len(listaDeExperimentos):
            listaDeExperimentos.pop(indice)
            print("\033[1;32m"+"Experimentos Eliminado con exito"+'\033[0;m')
        else:
            print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

#Funcion para visualizar mis experimentos
def visulizar_experimentos():
    
    tablaExperimentos = PrettyTable()
    
    tablaExperimentos.field_names = ["\033[1;33;40m"+"id", "Nombre", "Fecha", "Tipo","Resultados"+'\033[0;m']
    for i, experimento in enumerate(listaDeExperimentos, start=1):
        tablaExperimentos.add_row([i, experimento[0], experimento[1], experimento[2],experimento[3]], divider=True)
        
    print(tablaExperimentos)
    
   
#Funcion para calular estadisticas
def calcular_estadisticas():
    visulizar_experimentos()

    tablaEstadistica = PrettyTable()
    tablaEstadistica.field_names = ["\033[1;33;40m"+"id", "Promedio", "Maximo", "Minimo"+'\033[0;m']

    try:
        indice = int(input("Ingrese el indice del experimento a calcular estadisticas: ")) - 1
        if 0 <= indice < len(listaDeExperimentos):
            resultados = listaDeExperimentos[indice][3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            print(f"\033[1;32m Estadisticas del experimento: {listaDeExperimentos[indice][0]}"+'\033[0;m')
            tablaEstadistica.add_row([indice + 1, promedio, maximo, minimo])
            print(tablaEstadistica)
        else:
            print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')


#Funcion de comprar experimentos
def comparar_experimentos():
    visulizar_experimentos()
    tablaCompararExperimento = PrettyTable()
    tablaCompararExperimento.field_names = ["\033[1;33;40m"+"id", "Resultado", "Promedio"+'\033[0;m']

    
    try: 
        indices = list(map(int, input("Ingrese los indices de los experimentos a comprar separados por comas: ").split(",")))
        comprarciones = []
        for indice in indices:
            if 1 <= indice <= len(listaDeExperimentos):
                resultados = listaDeExperimentos[indice-1][3]
                promedio = sum(resultados) / len(resultados)
                comprarciones.append((listaDeExperimentos[indice-1][0],promedio))
            else:
                print("\033[1;33m"+"Error: Numero invalido"+'\033[0;m')
        comprarciones.sort(key=lambda x: x[1], reverse=True)
        for nombre, promedio in comprarciones:   
            tablaCompararExperimento.add_row([nombre, promedio])
            print(tablaCompararExperimento)
    except:
        print("\033[1;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')
    

#Funcion para generar informe
def generar_informe():
    if not listaDeExperimentos:
        print("\033[1;33m"+"No existen experimentos registrados"+'\033[0;m')
        return
    with open("informe.txt", "w") as archivo:
        archivo.write("==== Informe ====\n")
        archivo.write("=================\n")
        for experimento in listaDeExperimentos:
            resultados = experimento[3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            archivo.write(f"Nombre: {experimento[0]} \n")
            archivo.write(f"Fecha: {experimento[1]}\n")
            archivo.write(f"Tipo: {experimento[2]}\n")
            archivo.write(f"Resultados: {experimento[3]}\n")
            archivo.write(f"Promedio: {promedio}\n")
            archivo.write(f"Maximo: {maximo}\n")
            archivo.write(f"Minimo: {minimo}\n")
            archivo.write("=================\n")
        print("\033[1;32m"+"Informe generado con exito"+'\033[0;m')

#Funcion para mostrar el menu
def mostar_menu():
    
    tablaMenu = PrettyTable()
    tablaMenu.align = "l"
    tablaMenu.field_names = ["\033[1;37;40m"+"Menu Principal"+'\033[0;m']
    tablaMenu.add_row(["\033[3;31;36m"+"1. Agregar experimento"+'\033[0;m'])
    tablaMenu.add_row(["\033[3;31;36m"+"2. Visualizar experimentos"+'\033[0;m'])
    tablaMenu.add_row(["\033[3;31;36m"+"3. Eliminar experimentos"+'\033[0;m'])
    tablaMenu.add_row(["\033[3;31;36m"+"4. Calcular estadisticas"+'\033[0;m'])   
    tablaMenu.add_row(["\033[3;31;36m"+"5. Comparar experimentos"+'\033[0;m'])
    tablaMenu.add_row(["\033[3;31;36m"+"6. Generar informe"+'\033[0;m'])
    tablaMenu.add_row(["\033[3;31;36m"+"7. Salir"+'\033[0;m'])
        
    print(tablaMenu)

#Funcion principal
def main():
    while True:

        mostar_menu()
        try:
            opcion = int(input("\033[3;35;47m"+"Ingrese una opcion: "+'\033[0;m'))
            if opcion == 1:
                agregar_experimento()
            elif opcion == 2:
                visulizar_experimentos()
            elif opcion == 3:
                eliminar_experimento()
            elif opcion == 4:
                calcular_estadisticas()
            elif opcion == 5:
                 comparar_experimentos()
            elif opcion == 6:
                generar_informe()
            elif opcion == 7:
                print("\033[3;33;46m"+"Gracias por usar el programa ¡Vuelva pronto!" +'\033[0;m')
                break
        except: 
            print("\033[3;33m"+"Error: Entrada no valida. intenta de nuevo"+'\033[0;m')

main()      