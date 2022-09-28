#Imprime las lineas de un archivo con su número

archivo = open("archivo.txt")
i = 1

for linea in archivo:
    linea = linea.rstrip("\\n")
    print(" %4d: %s" % (i, linea))
    i+=1

archivo.close()

# alternativa
archivo = open("archivo.txt")

for i, linea in enumerate(archivo):
    linea = linea.rstrip("\\n")
    print(" %4d: %s" % (i, linea))

archivo.close()