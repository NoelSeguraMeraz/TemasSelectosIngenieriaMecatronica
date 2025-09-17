import time
import socket

#Setup
esp32 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
esp32.connect(('192.168.0.100', 1234))

#Comandos
esp32.send(("ROJO" + '\n').encode())
time.sleep(5)
esp32.send(("AZUL" + '\n').encode())
time.sleep(5)
esp32.send(("VERDE" + '\n').encode())

#Limpieza
esp32.close()
