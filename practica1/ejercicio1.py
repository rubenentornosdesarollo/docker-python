# Guardamos lo que nos meten los usuarios en variables
nombreArchivo = str(input("Introduce el nombre del archivo a abrir: "))
bucle = int(input("¿Cuantas lineas quieres sacar?"))

# Guardamos el archivo en la variable
archivo = open(nombreArchivo)

# Guardamos todas las lineas del archivo
linea=archivo.readlines()

print(linea[0:bucle])

# Cerramnos el archivo
archivo.close()

