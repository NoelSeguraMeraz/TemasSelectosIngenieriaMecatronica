import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Dibujar un círculo en el centro
    h, w, _ = frame.shape
    cv2.circle(frame, (w//2, h//2), 50, (0, 255, 0), 2)

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
