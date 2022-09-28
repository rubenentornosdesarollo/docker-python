archivo = open("archivo.txt")

# tres formas

linea=archivo.readline()
while linea != '':
    # procesar linea
    linea=archivo.readline()
    print(linea)

for linea in archivo:
    # procesar linea
    print(linea)

lineas = archivo.readlines() #usar readlines solo cuando el archivos sea pequeño
for linea in lineas:
    # procesar linea
    print(linea)

# liberar memoria siempre
# ficheros pequeños tienen un pequeño impacto
# con ficheros grandes cuidado con la memoria
archivo.close()
