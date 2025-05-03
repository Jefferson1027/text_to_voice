'''
Archivo Principal donde van a correr las funcionalidades diseñadas en los otros scripts
1. Va a coger la url ingresada por el usuario y la va a abrir
2. Va a extraer el texto de la url
3. Va a convertir el texto a voz
4. Va a guardar el archivo mp3
'''
from abrir_url import open_url #-- Abrir la url
from extractor_texto import extract_text # -- Para trabajar el contenido
from texto_a_voz import convert_to_mp3  #-- Para convertirlo a mp3


# Intentar recibir la url del usuario y abrirla
articulo = input("Ingresa la url del artículo a convertir en mp3\n")
url = open_url(articulo)

# Extraer el texto 
texto = extract_text(url)

# Convertir el texto a mp3 y guardarlo
mp3 = convert_to_mp3(texto)














