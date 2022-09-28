import csv

# Guardamos el nombre del archivo a usar
nombreArchivo = str(input("Introduce el nombre del archivo a abrir: "))

# Guardamos las filas a sacar
eleccion = str(input("Introduce que quieres sacar: ")).split(",")

with open(nombreArchivo, mode='r') as csv_file:
    # Ceramos que el archivo csv se convierta en un diccionario separado por ;
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    # Leemos las cabeceras y si estan imprimimos su contenido
    for row in csv_reader:
        for i in eleccion:
            print(row[i])
