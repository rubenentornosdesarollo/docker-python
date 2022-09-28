# Guardamos el nombre del archivo a usar
nombreArchivo = "fundacion.txt"

# Guardamos el archivo en la variable
archivo = open(nombreArchivo, "rt")

# Contamos cuantas lineas tiene el archivo
print(len(archivo.readlines()))

# Contamos el numero de palabras del archivo
numerosPalabras = 0
caracteres = 0
archivo.seek(0)
datos = archivo.readlines()
for linea in datos:
    palabras = linea.split()
    numerosPalabras += len(palabras)

    # Por cada palabra contamos su longitud
    for palabra in palabras:
        caracteres += len(palabra)

# Imprimimos el resultado
print(numerosPalabras)
print(caracteres)


# Cerramos el archivo
archivo.close()