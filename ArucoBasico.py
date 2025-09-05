import cv2
import time

# Abrir la cámara
cap = cv2.VideoCapture(0)

# Definir FPS deseados
fps = 15
frame_time = 1 / fps

# Cargar el diccionario de ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()

# Crear el detector
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

while True:
    start = time.time()

    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises (opcional, mejora rendimiento)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar marcadores
    corners, ids, rejected = detector.detectMarkers(gray)

    # Dibujar detecciones si existen
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

    # Mostrar el video
    cv2.imshow("Deteccion ArUco", frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

    # Controlar framerate
    elapsed = time.time() - start
    delay = max(0, frame_time - elapsed)
    time.sleep(delay)

cap.release()
cv2.destroyAllWindows()
