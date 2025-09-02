import cv2
import time
import numpy as np

# Abrir la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

# Definir FPS deseados
fps = 15
frame_time = 1 / fps

while True:
    start = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    # Convertir de BGR (formato por defecto en OpenCV) a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Forzar la saturación al 100%
    hsv[:, :, 1] = 255

    # Convertir de nuevo a BGR para mostrar
    saturated = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Mostrar la imagen procesada
    cv2.imshow("Video Saturacion Maxima", saturated)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Controlar framerate
    elapsed = time.time() - start
    delay = max(0, frame_time - elapsed)
    time.sleep(delay)

cap.release()
cv2.destroyAllWindows()
