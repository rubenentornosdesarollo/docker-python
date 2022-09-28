#Módulo que utiliza el módulo de log

from distutils.log import error
import log

# Constante que contiene el nombre del archivo de log a utilizar
ARCHIVO_LOG = "mi_log.txt"

def main():
    # Al comenzar, abrir el log
    archivo_log = log.abrir_log(ARCHIVO_LOG)
    # ...
    # Hacer cosas que pueden dar error
    error="Mira lo que se avesina"
    if error:
        log.guardar_log(archivo_log, "ERROR: " + error)
    # ...
    # Finalmente cerrar el archivo
    log.cerrar_log(archivo_log)

main()