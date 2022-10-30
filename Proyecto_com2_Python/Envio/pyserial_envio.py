def envio_arduino(mensaje):
    import serial, time 
    message =mensaje
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

    