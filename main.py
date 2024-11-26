from datetime import datetime
import statistics


class Experimentos:



#función de inicializacion
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados
 


#función para agregar un experimento
def agregarExperimento(listaExperimentos):
    nombre = input("Ingrese el nombre del experimento")
    fechaRealizacion_str = input("Ingrese la fecha de realización del experimento (DD/MM/YYYY)")
    try: 
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("fecha no valida.")
        return
    tipoExperimento = input("Ingrese el Tipo de experimento: ")
    resultados_str = input("ingrese los valores, separados por comas: ")
    try: 
        resultados = list(map(float, resultados_str.split(",")))
    except ValueError:
        print("Resultado no valido.")
        return

#crear un objeto
    experimento = Experimentos(nombre, fechaRealizacion, tipoExperimento, resultados)
    listaExperimentos.append(experimento)
    print("Experimento agregado con exito..")

def VisualizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay Experimentos registrados")
        return
    
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha de realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo de Experimento: {experimento.tipoExperimento}")
        print(f"Resultados del Experimento: {experimento.resultados}")

def analizarResultados(listaExperimentos):
    if not listaExperimentos:
        print("No hay Experimentos registrados")
        return
     
    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nAnalisis del Experimento {experimento.nombre} ")
        print(f"\nAnalisis del Experimento {experimento.nombre} ")
        print(f"Promedio de resultados {promedio} ")
        print(f"Valor máximo {maximo} ")
        print(f"Valor mínimo {minimo} ")


def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("No hay Experimentos registrados")
        return
    
    #abrir archivo txt para escribir informe
    with open("informe_experimentos.txt", "w") as archivo:
        #escribir los detalles del experimento en el archivo
        for experimento in listaExperimentos:
            archivo.write(f"Nombre : {experimento.nombre}\n")
            archivo.write(f"Fecha de realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo de Experimento: {experimento.tipoExperimento}\n")
            archivo.write(f"Resultados del Experimento: {experimento.resultados}\n")
            archivo.write("\n")
    print("Informe generado como 'informe_experimentos.txt'") 

def menu():

    listaExperimentos = [] 
    while True:
        print("\nMENU DE OPCIONES")
        print("1. AGREGAR EXPERIMENTO")
        print("2. VISUALIZAR EXPERIMENTO")
        print("3. ANALISIS DE RESULTADOS")
        print("4. GENERAR INFORME")
        print("5. SALIR")


        opcion = input("SELECIONE UNA OPCIÓN: ")
    
        if opcion == "1":
            agregarExperimento(listaExperimentos)
        elif opcion == "2":
            VisualizarExperimentos(listaExperimentos)
        elif opcion == "3":
            analizarResultados(listaExperimentos)
        elif opcion == "4":
            generarInforme(listaExperimentos)
        elif opcion == "5":
            print("SALIENDO DEL PROGRAMA")
            break
        else:
            print("OPCION INVALIDA")


menu()          



        







