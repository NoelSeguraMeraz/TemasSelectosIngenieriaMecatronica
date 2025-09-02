import cv2
import time

# Abrir la cámara (0 = cámara por defecto)
cap = cv2.VideoCapture(0)

# Definir FPS deseados
fps = 10  
frame_time = 1 / fps  

while True:
    start = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar el frame
    cv2.imshow("Camara", frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Calcular tiempo y esperar lo necesario para mantener fps
    elapsed = time.time() - start
    delay = max(0, frame_time - elapsed)
    time.sleep(delay)

cap.release()
cv2.destroyAllWindows()
