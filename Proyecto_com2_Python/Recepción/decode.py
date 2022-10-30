from os import environ 
import math
from hammingdeco import hammingdeco 
from decodemorse import decoder
###################################################################
import serial
import time
import re
Pattern = ["([0-1]+)\\r\\n", "([a-z]+)\\r\\n"]


def read_arduino():
    arduino = serial.Serial('COM3', 9600)
    time.sleep(0.5)
    mensaje = False
    leyendo = True
    recibido = []
    while leyendo:
        write = arduino.readline().decode("utf-8")
        try:
            true_write = re.findall(Pattern[1], write)[0]
            if true_write != "nomessage" and true_write != "receptor":
                mensaje = True
                print("leyendo")
            else:
                mensaje = False
                print("sin leer")
        except Exception:
            pass
        while mensaje:
            write = arduino.readline().decode("utf-8")
            try:
                true_write = re.findall(Pattern[0], write)[0]
                if len(true_write) == 7:
                    print(true_write)
                    recibido.append(true_write)
            except Exception:
                pass
            try:
                true_write = re.findall(Pattern[1], write)[0]
                if true_write == "nomessage":
                    print("Se acabo la lectura")
                    mensaje = False
                    leyendo = False
                    print(recibido)
            except Exception:
                pass
    arduino.close()
    return recibido


def main():
    envio=read_arduino()


    tren=hammingdeco(envio)
    n= len(tren)
    m = (n/6)
    m= math.floor(m) 
    segmento=[]
    for d in range(m):
        p= 6*d
        segmento.append(tren[p:p+6])

    #print(segmento)

    texto_morse = []

    for f in segmento:
        char_morse = ''
        for g in f:

            if g != '1':
                char_morse+= '-'
            else:
                char_morse+= '.'
        texto_morse.append(char_morse)
        

    #print(texto_morse)
    palabra = ''

    for e in texto_morse:
        #print(e)
        palabra += e + ' '

    print(palabra)
    decoder(palabra)



if __name__ == "__main__":
    main()
#############################################################