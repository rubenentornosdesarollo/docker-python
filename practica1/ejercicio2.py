# Guardamos el nombre del archivo a usar
nombreArchivo = str(input("Introduce el nombre del archivo a abrir: "))

# Guardamos el archivo en la variable
archivo = open(nombreArchivo)

# Guardamos todas las lineas del archivo
linea=archivo.readlines()

# Creamos un nuevo archivo, donde vamos a escribir
archivoCopia = open("archivocopia.txt", "w")

# EScribimos en el archivo destino todo lo que havia en el primer archivo
archivoCopia.writelines(linea)

# Cerramnos el archivo
archivo.close()
archivoCopia.close()