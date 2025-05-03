'''
Creador del objeto de audio para guardarlo
'''

import gtts    #-- convierte texto a voz

def convert_to_mp3(texto):
    #Convertir el texto que llega a audio
    tts = gtts.gTTS(text= texto, lang= "es", slow= False)

    tts.save('Audios/audio.mp3') # guardar el audio