# Guardamos el nombre del archivo a usar
nombreArchivo = "fundacion.txt"

# Guardamos el archivo en la variable
archivo = open(nombreArchivo, "rt")

expresion = input("Escribe lo que quieres buscar: ")

datos = archivo.readlines()

for linea in datos:
    palabras = linea.split()
    # Comprobamos que la palabra sea igual que la palabra que hemos introduciddo
    for palabra in palabras:
        if(palabra==expresion):
            print(linea)


archivo.close()
