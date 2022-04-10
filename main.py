import pathlib
from pathlib import Path
import os

def get_download_path(downloads_guid):
    #Devuelve la ruta por defecto de la carpeta del registro de Windows seleccionado.

    import winreg
    sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
        location = winreg.QueryValueEx(key, downloads_guid)[0]
    return location

def check_number_name(name_file):
    #Verifica si en el nombre existe algún número.
    if any(chr.isdigit() for chr in name_file) == True:
        return True

if __name__ == "__main__":

    paramRegister = 'personal'  # Documentos
    rutaDocuments = get_download_path(paramRegister)
    #Verificamos si existe el fichero de "diogenes.cong". Si existe leemos el contenido, si no existe  lo creamos en la carpeta "Descargas".
    if Path(rutaDocuments + "\\diogenes.conf").is_file() == True:
        with open(rutaDocuments + "\\diogenes.conf","r") as ficheroConfiguracion:
            for linea in ficheroConfiguracion:
                #Obtenemos la ruta definida en el fichero de configuración.
                rutaAux = linea.split("\"")
                ruta = rutaAux[1]
    else:
        #Buscamos las rutas por defecto de las carpetas "Documentos" y "Descargas".
        paramRegister = 'personal'  # Documentos
        rutaDocuments = get_download_path(paramRegister)
        paramRegister = '{374DE290-123F-4565-9164-39C4925E467B}'  # Descargas
        rutaDownloads = get_download_path(paramRegister)

        #Creamos el fichero "diogenes.conf" en la carpeta "Documentos" con la ruta de la carpeta "Descargas".
        file = open(rutaDocuments + "\\diogenes.conf", "w")
        file.write("directorio = \"" + rutaDownloads + "\"")
        file.close()

        #Por defecto se van a listar las imagenes de la carpeta Descargas.
        ruta = rutaDownloads

    tipoImagenes = ".png,.jpeg,.jpg,.JPEG"
    contador = 0
    for archivo in os.listdir(ruta):
        extension = pathlib.Path(archivo)
        #Verificamos si es una imagen y si es un archivo, para descartar los directorios.
        if extension.suffix in tipoImagenes and Path(ruta + "//" + archivo).is_file() == True:
            if check_number_name(archivo) == True:
                contador += 1
                archivoMayus = archivo.upper()
                if contador % 2 == 0:
                    archivoMayus = "=>" + archivoMayus
                print(archivoMayus)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
