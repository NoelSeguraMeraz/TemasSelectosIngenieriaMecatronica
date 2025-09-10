import pygame
import sys
import cv2

# Inicializar pygame
pygame.init()

# Configuración de ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame + OpenCV")

# Captura de cámara con OpenCV
cap = cv2.VideoCapture(0)

# Colores
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Fuente
font = pygame.font.SysFont(None, 30)

# Clase botón
class Button:
    def __init__(self, text, x, y, w, h, color, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Posición inicial de la figura
x, y = WIDTH // 2, HEIGHT // 2
vel = 5

# Funciones de dibujo
def draw_circle():
    pygame.draw.circle(screen, RED, (x, y), 50)

def draw_square():
    pygame.draw.rect(screen, GREEN, (x - 50, y - 50, 100, 100))

def draw_triangle():
    points = [(x, y - 60), (x - 60, y + 60), (x + 60, y + 60)]
    pygame.draw.polygon(screen, BLUE, points)

# Crear botones
buttons = [
    Button("Círculo", 20, 20, 120, 40, GRAY, draw_circle),
    Button("Cuadro", 160, 20, 120, 40, GRAY, draw_square),
    Button("Triángulo", 300, 20, 120, 40, GRAY, draw_triangle)
]

# Variable para guardar qué dibujar
current_action = None

# Loop principal
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # =====================
    # Capturar y procesar video con OpenCV
    # =====================
    ret, frame = cap.read()
    if ret:
        # Procesar el video (ejemplo: convertir a escala de grises)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

        # Convertir de OpenCV (numpy) a Surface de Pygame
        frame_rgb = cv2.resize(frame_rgb, (320, 240))
        frame_surface = pygame.surfarray.make_surface(frame_rgb.swapaxes(0, 1))

        # Mostrar video en la esquina
        screen.blit(frame_surface, (WIDTH - 340, 20))

    # Dibujar botones
    for button in buttons:
        button.draw(screen)

    # Dibujar la figura seleccionada
    if current_action:
        current_action()

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(pos):
                    current_action = button.action

    # Movimiento con teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  x -= vel
    if keys[pygame.K_RIGHT]: x += vel
    if keys[pygame.K_UP]:    y -= vel
    if keys[pygame.K_DOWN]:  y += vel

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
sys.exit()
