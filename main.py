import csv
import matplotlib.pyplot as plt

def diccionario_notas_desde_CSV(archivoCSV):
    with open(f"{archivoCSV}", "r", encoding="utf-8") as n:
        notas = csv.reader(n)
        next(notas)  # Para saltarse el header

        dict_notas = dict()

        for fila in notas:
            if not fila: # Si hay un salto de linea lo omitimos
                continue

            nombre = fila[0].title().strip()
            try:
                nota = float(fila[2]) # Comprueba que el flaot sea realemente un float
                if nombre not in dict_notas:
                    dict_notas[nombre] = list()
                dict_notas[nombre].append(nota)
            except ValueError:
                continue
        return dict_notas

def diccionario_becas_desde_TXT(archivoTXT):
    with open(f"{archivoTXT}", "r", encoding="utf-8") as b:
        becas = b.readlines()

        dict_becas = dict()

        for linea in becas:
            linea = linea.split(":") # Separamos la linea por : a un array
            nombre_beca = linea[0].title().strip() 
            dict_becas[nombre_beca] = linea[1].strip()
        return dict_becas

def generar_informe(dict_notas, dict_becas):
    header = f"{'ALUMNO':<12} | {'NOTA':<6} | {'ESTADO':<10} | {'BECA':<5}"
    print(header)
    print("-" * len(header))

    nombre_array = []
    nota_media_array = []
    for nombre, notas in dict_notas.items():
        nota_media = round(sum(notas) / len(notas), 2)
        nota_media_array.append(nota_media)
        
        estado = "APROBADO" if nota_media >= 5 else "SUSPENSO"
        try:
            beca = dict_becas[nombre]
        except KeyError:
            beca = "NO"

        if beca == "SI":
            nombre_array.append(nombre + "(*)")
        else:
            nombre_array.append(nombre)
        
        print(f"{nombre:<12} | {nota_media:<6} | {estado:<10} | {beca:<5}")
    
    plt.xticks(rotation=45, ha='right')
    color = ['green' if m >= 5 else 'red' for m in nota_media_array]
    plt.bar(nombre_array, nota_media_array, color=color)
    plt.xlabel('Nombre alumnos')
    plt.ylabel('Nota Promedio')
    plt.axhline(y=5, color='blue', linestyle='--')
    plt.title("Calificaciones Finales y Estado de Beca")
    plt.savefig("./notes_graph.png")
    plt.show()




try:
    dict_notas = diccionario_notas_desde_CSV("files/ej30notasdaw.csv")
    dict_becas = diccionario_becas_desde_TXT("files/ej30becas.txt")

    generar_informe(dict_notas, dict_becas)
except FileNotFoundError:
    print(FileNotFoundError)

