import serial
import time

# Ajusta el puerto (Windows: "COM3", Linux/Mac: "/dev/ttyUSB0")
ser = serial.Serial("COM3", 115200, timeout=1)
time.sleep(2)  # Esperar que la ESP32 arranque

while True:
    # Mandamos petición
    ser.write(b"R")
    
    # Leemos respuesta
    line = ser.readline().decode().strip()
    if line:
        try:
            b1, b2, b3, a1, a2 = map(int, line.split(","))
            print(f"Botones: {b1}, {b2}, {b3} | Analógicos: {a1}, {a2}")

            # Ejemplo de procesamiento:
            if b1 == 0:  # Botón presionado
                print("⚡ Botón 1 presionado")
            if a1 > 2000:
                print("🎚️ Potenciómetro 1 en nivel alto")

        except ValueError:
            print("Error en datos:", line)
    
    time.sleep(0.5)  # Cada medio segundo
