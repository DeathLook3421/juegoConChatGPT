import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir constantes de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Definir la velocidad de la pelota
VELOCIDAD_PELOTA = 5

# Definir la clase Pelota
class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.set_colorkey(NEGRO)
        pygame.draw.circle(self.image, BLANCO, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2)

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Si la pelota sale de los límites de la pantalla, aparece en el lado opuesto
        if self.rect.right < 0:
            self.rect.left = ANCHO_PANTALLA
        elif self.rect.left > ANCHO_PANTALLA:
            self.rect.right = 0
        elif self.rect.bottom < 0:
            self.rect.top = ALTO_PANTALLA
        elif self.rect.top > ALTO_PANTALLA:
            self.rect.bottom = 0

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Control de pelota con teclado")

# Inicializar reloj
reloj = pygame.time.Clock()

# Crear la pelota
pelota = Pelota()

# Crear un grupo de sprites y añadir la pelota al grupo
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(pelota)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover la pelota según las teclas presionadas
    dx = 0
    dy = 0
    if teclas[pygame.K_UP]:
        dy = -VELOCIDAD_PELOTA
    if teclas[pygame.K_DOWN]:
        dy = VELOCIDAD_PELOTA
    if teclas[pygame.K_LEFT]:
        dx = -VELOCIDAD_PELOTA
    if teclas[pygame.K_RIGHT]:
        dx = VELOCIDAD_PELOTA

    # Actualizar la posición de la pelota
    pelota.update(dx, dy)

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar todos los sprites
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    reloj.tick(60)
