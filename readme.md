# TEXTO A VOZ

## Descripción

La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible en formato mp3.


## Requisitos
Se recomienda crear un entorno virtual para que no haya conflictos con otras bibliotecas instaladas en tu sistema.

`python -m venv venv`

### Activar entorno virtual

Se recomienda estar en la raiz del proyecto para hacer lo siguiente:

1. En windows

`venv\Scripts\activate`

2. En macOs/Linux

`Source venv/bin/activate`

### Instalación de dependencias

Para ejecutar este proyecto, necesitas instalar las siguientes bibliotecas:
- `nltk` (kit de herramientas de lenguaje natural)
- `newspaper3k`
- `gtts` (Google Text-to-Speech)
- `lxml`
- `urllib3`

Puedes instalar todas las dependencias utilizando el archivo `requirements.txt`:
```sh
pip install -r requirements.txt
```

Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para 
luego manejar la conversión de texto a voz.

## Uso

- Proporciona una URL de un artículo que deseas convertir a mp3.
- El programa abrirá la URL, extraerá el texto del artículo y lo convertirá a un archivo de audio en formato mp3.

## Ejecución
Situate en la raiz del proyecto y escribe lo siguente en la terminal:
`python main.py`

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Sube tus cambios a tu fork (git push origin feature/nueva-funcionalidad).
5. Crea un Pull Request.