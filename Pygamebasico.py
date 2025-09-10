import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de ventana
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo Botones")

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

# Funciones de dibujo
def draw_circle():
    pygame.draw.circle(screen, RED, (WIDTH//2, HEIGHT//2), 50)

def draw_square():
    pygame.draw.rect(screen, GREEN, (WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100))

def draw_triangle():
    points = [(WIDTH//2, HEIGHT//2 - 60),
              (WIDTH//2 - 60, HEIGHT//2 + 60),
              (WIDTH//2 + 60, HEIGHT//2 + 60)]
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

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
