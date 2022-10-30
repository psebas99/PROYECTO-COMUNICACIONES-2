#LLAMADA A LAS CLASES DE HUFFMAN Y HAMMING
from hamming import hamming
from codemorse import hoffman 
from pyserial_envio import envio_arduino
import serial, time 
#INGRESO DEL TEXTO A CODIFICAR
texto= input("Inserte el mensaje aquí:" )
archivo = hoffman(texto)

#SE GENERA LA MATRIZ QUE SE ENVIARA AL PY-SERIAL
envio = []
for i in archivo:
    mensaje_codificado=hamming(i)
    envio.append(mensaje_codificado)
# "envio" ES LA MATRIZ QUE LLEVA EL TEXTO YA CODIFICADO POR COMPLETO 

#print(envio)
##############################

message =envio
n = 0
write = None


def main():
    arduino = serial.Serial('COM5', 9600)
    time.sleep(0.5)
    for n in message:
        print(n)
        write = "{}".format(n).encode("utf-8")
        arduino.write(write)
        time.sleep(5)
    arduino.close()


if  __name__ == "__main__":
        main()


