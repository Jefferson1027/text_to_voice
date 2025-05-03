'''
Este archivo es creado para abrir, checar que la url es correcta
y posteriormente retornarla para su manejo en el archivo principal
'''
#Importar la librería para trabajar con urls
from urllib import request # especificamente este modulo porque no necesitamos toda la libreria urllib

def open_url(url):
    # En esta funcion intentaremos abrir la url y retornarla
    try:
        url = request.urlopen(url)
        if url:
            return url.url
    except ValueError:
        raise (f"No ha ingresado una url válida")
    except TypeError:
        raise (f"Ha ocurrido un error\nSolicitamos que lo intente de nuevo mas tarde")
    

