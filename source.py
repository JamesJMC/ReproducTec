import RPi.GPIO as GPIO
import time
import pygame
from os import listdir
from os.path import isfile, join
from os import scandir, getcwd
from os.path import abspath
GPIO.setmode(GPIO.BCM)
GPIO.cleanup

#funcion para poner en play la cancion
def play_Audio():
    #pygame.mixer.init()
    global cont
    global vol
    print("PLAY")
    print("Cancion actual "+str(cont+1))
    #print(len(solo_archivos))
    if pygame.mixer.music.get_busy() == True:
        print("Poner play de nuevo")
        pygame.mixer.music.unpause()               #se hace un stop a la cancion que esta sonando
    else:
        pygame.mixer.music.load(solo_archivos[cont])
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play()
        if cont == len(solo_archivos)-1:
            #cont = 0
            pygame.mixer.music.queue(solo_archivos[0])
        else:
            #cont = cont +1
            pygame.mixer.music.queue(solo_archivos[cont])##cont+1
    #while pygame.mixer.music.get_busy() == True:        #si se esta reproduciendo la cancion continua
    #    continue
    #cont = cont +1;                                     #cuando termina se pasa a la siguiente cancion



#funcion para pausar el audio
def pause_Audio():
    print("Pausa")
    #if(GPIO.input(btnPause) == True):
    if pygame.mixer.music.get_busy() == True:   #si se esta reproduciendo la musica, se pone en pausa
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()


#funcion para subir volumen
def volumeUp_Audio():
    print("Volumen +")
    global vol
    if vol < 1.0:
        vol += 0.1
        print("Volumen: ",vol)
        if vol == 0.10000000000000003:
            GPIO.output(led1, 1)
        if vol == 0.20000000000000004:
            GPIO.output(led2, 1)
        if vol == 0.30000000000000004:
            GPIO.output(led3, 1)
        if vol == 0.4:
            GPIO.output(led4, 1)
        if vol == 0.5:
            GPIO.output(led5, 1)
        if vol == 0.6:
            GPIO.output(led6, 1)
        if vol == 0.7 or vol == 0.7999999999999999:
            GPIO.output(led7, 1)
        
        pygame.mixer.music.set_volume(vol)
    else:
        print("Volumen maximo")


#funcion para bajar volumen
def volumeDown_Audio():
    print("Volumen -")
    global vol
    if vol > 0.0:
        vol -= 0.1
        print("Volumen: ",vol)
        if vol == 2.7755575615628914e-17:
            GPIO.output(led1, 0)
        if vol == 0.10000000000000003:
            GPIO.output(led2, 0)
        if vol == 0.20000000000000004:
            GPIO.output(led3, 0)
        if vol == 0.30000000000000004:
            GPIO.output(led4, 0)
        if vol == 0.4:
            GPIO.output(led5, 0)
        if vol == 0.5:
            GPIO.output(led6, 0)
        if vol == 0.6:
            GPIO.output(led7, 0)
        if vol == 0.7 or vol == 0.7999999999999999:
            GPIO.output(led7, 0)
        
        pygame.mixer.music.set_volume(vol)
    else:
        print("Volumen minimo")


#funcion para pasar a la cancion siguiente
def next_Audio():
    print("Cancion siguiente")
    global cont
    print("largo: ",cont+1,len(solo_archivos))
    if cont+1 == len(solo_archivos):            #si esta ubicado en la ultima posicion de la lista (ultima cancion) se inicia en 0 (primer cancion)
        print("jaskdhkjahskdjfhakjshdkjfhakjsdhfkjahskjdhfkjahsdkjfas")
        print("Inicializar en 0: "+str(cont))
        cont = 0
        print("Valor de cont = "+str(cont))
        pygame.mixer.music.stop()               #se hace un stop a la cancion que esta sonando
        play_Audio()         #se manda a reproducir la siguiente cancion
                
    else:#pygame.mixer.music.get_busy() == True:   #si esta en reproccion
        print("ENTRA AQUI")
        pygame.mixer.music.stop()               #se hace un stop a la cancion que esta sonando
        cont += 1                                 #siguiente cancion en la lista
        print("Valor de cont = "+str(cont))
        play_Audio()


#funcion para pasar a la cancion anterior
def preview_Audio():
    print("Cancion anterior")
    global cont
    global vol
    if (cont == 0):
        cont = len(solo_archivos)-1
        pygame.mixer.music.stop()
        play_Audio()
    else:
        cont -= 1
        pygame.mixer.music.stop()
        play_Audio()          


#DIRECCION DE LA CARPETA DE MUSICA
path = "/home/pi/Desktop/Proyecto/music"

#VARIABLES DE LOS BOTONES
btnPlay = 14
btnPause = 15
btnVolumeUp = 24
btnVolumeDown = 12
btnNext = 16
btnPreview = 26

#CONFIGURAR LOS PINES
GPIO.setup(btnPlay, GPIO.IN, pull_up_down=GPIO.PUD_UP)           #ACTIVAR LAS RESISTENCIAS PUD_UP
GPIO.setup(btnPause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnVolumeUp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnVolumeDown, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnNext, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnPreview, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#VARIABLES DE LOS LEDS
led1 = 17
led2 = 27
led3 = 22
led4 = 5
led5 = 6
led6 = 13
led7 = 19

#CONFIGURAR LOS PINES
GPIO.setup(led1, GPIO.OUT)           #ACTIVAR LAS RESISTENCIAS PUD_UP
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(led5, GPIO.OUT)
GPIO.setup(led6, GPIO.OUT)
GPIO.setup(led7, GPIO.OUT)

#lista de los archivos en la carpeta
solo_archivos = [abspath(arch.path) for arch in scandir(path) if arch.is_file()]



#inicializar el mixer
pygame.mixer.init()



#INDICE DE LA LISTA CON LOS ARCHIVOS
vol = 0.6
cont = 0
print(solo_archivos[cont])


#PONER VOLUMEN VISUALIZADO EN LOS LEDS
GPIO.output(led1, 1)
GPIO.output(led2, 1)
GPIO.output(led3, 1)
GPIO.output(led4, 1)
GPIO.output(led5, 1)
GPIO.output(led6, 1)
GPIO.output(led7, 0)

#VARIABLES BOOLEANAS PARA CADA INPUT
boolBtnPlay = True
boolBtnPause = True
boolBtnVolUp = True
boolBtnVolDown = True
boolBtnNext = True
boolBtnPreview = True


        #AGREGAR EVENTOS A LOS BOTONES
while True:
    boolBtnPlay = GPIO.input(btnPlay)
    boolBtnPause = GPIO.input(btnPause)
    boolBtnVolUp = GPIO.input(btnVolumeUp)
    boolBtnVolDown = GPIO.input(btnVolumeDown)
    boolBtnNext = GPIO.input(btnNext)
    boolBtnPreview = GPIO.input(btnPreview)
    
    
    if boolBtnPlay == False:
        boolBtnPlay =True
        play_Audio()
    elif boolBtnPause == False:
        boolBtnPause = True
        pause_Audio()
    elif boolBtnVolUp == False:
        volumeUp_Audio()
    elif boolBtnVolDown == False:
        volumeDown_Audio()
    elif boolBtnNext == False:
        next_Audio()
    elif boolBtnPreview == False:
        preview_Audio()
    time.sleep(0.15)

GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
GPIO.output(led4, 0)
GPIO.output(led5, 0)
GPIO.output(led6, 0)
GPIO.output(led7, 0)

GPIO.cleanup