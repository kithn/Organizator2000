import pathlib
from pathlib import Path
import os

def get_download_path():
    #Devuelve la ruta por defecto de la carpeta Descargas de Linux o Windows.
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def check_number_name(name_file):
    #Verifica si en el nombre existe algún número.
    if any(chr.isdigit() for chr in name_file) == True:
        return True

if __name__ == "__main__":
    ruta = get_download_path()
    if os.name == 'nt':
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
    else:
        os.system("ls " + ruta)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
