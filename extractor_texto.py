'''
Archivo creado para extraer la informacion de la url proporcionada por el usuario
y crear el archivo de texto para su posterior conversion a audio
'''

import newspaper as nwp     #-- Ayudara a extraer y analizar el contenido

def extract_text(url):
    articulo = nwp.Article(url,language = 'es') # Especificar el idioma a español (es)
    
    # descargar y analizar el contenido
    articulo.download()
    articulo.parse()
    #Escribir el texto
    texto = articulo.text
    
    return texto #devolver el articulo