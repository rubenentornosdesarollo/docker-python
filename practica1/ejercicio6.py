# Guardamos el nombre del archivo a usar
nombreArchivo = "letraAsereje.txt"

# Elegimos como guardar el nuevo archivo
nombreGuardado = input("Escribe el nombre con el que guardar el archivo: ")

datos = []

# Abrimos el archivo a encriptar como forigen
with open(nombreArchivo) as forigen:
    # Se lee entero
    lineas = forigen.readlines()

    # Separamos las lineas y las guardamos como lista
    for linea in lineas:
        lista = linea.split()

        # Por cada palabra en la lista
        for palabra in lista:
            nuevaPalabra = ""

            # Leemos los caracteres de la plabra, los pasamos a su codigo unicode, le sumamos 13
            for letra in palabra:
                codUnicode = ord(letra)
                codUnicode += 13 
                
                # Luego modulamos el numero
                codUnicode = codUnicode % 26

                # Y pasamos el numero que nos ha dado a character y formamos la nueva palabra
                unicodeLetra = chr(codUnicode)
                nuevaPalabra += unicodeLetra

                # Colgamo esa misma palabra de datos anteriormente creado
            datos.append(nuevaPalabra)
    
# Guardamos el nuevo fichero totalmente encriptado
with open(nombreGuardado + ".txt", "w") as fdestino:
    nuevoDatos = " ".join(datos)
    fdestino.writelines(nuevoDatos)
