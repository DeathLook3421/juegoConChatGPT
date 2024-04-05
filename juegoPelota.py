import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Definir constantes de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Definir la velocidad de la serpiente
VELOCIDAD_SERPIENTE = 5
INCREMENTO_VELOCIDAD = 1

# Definir la clase Serpiente
class Serpiente(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2)
        self.dx = VELOCIDAD_SERPIENTE
        self.dy = 0
        self.longitud = 1
        self.segmentos = [(self.rect.x, self.rect.y)]

    def update(self):
        # Actualizar posición de la serpiente
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Actualizar segmentos
        self.segmentos.insert(0, (self.rect.x, self.rect.y))
        if len(self.segmentos) > self.longitud:
            self.segmentos.pop()

    def crecer(self):
        self.longitud += 1

# Definir la clase Comida
class Comida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO_PANTALLA - self.rect.width)
        self.rect.y = random.randint(0, ALTO_PANTALLA - self.rect.height)

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Snake")

# Inicializar reloj
reloj = pygame.time.Clock()

# Crear la serpiente
serpiente = Serpiente()

# Crear la comida
comida = Comida()
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(serpiente, comida)

# Velocidad inicial
velocidad_actual = VELOCIDAD_SERPIENTE

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()

    # Mover la serpiente según las teclas presionadas
    if teclas[pygame.K_UP] and serpiente.dy == 0:
        serpiente.dx = 0
        serpiente.dy = -velocidad_actual
    elif teclas[pygame.K_DOWN] and serpiente.dy == 0:
        serpiente.dx = 0
        serpiente.dy = velocidad_actual
    elif teclas[pygame.K_LEFT] and serpiente.dx == 0:
        serpiente.dx = -velocidad_actual
        serpiente.dy = 0
    elif teclas[pygame.K_RIGHT] and serpiente.dx == 0:
        serpiente.dx = velocidad_actual
        serpiente.dy = 0

    # Colisiones con la comida
    if pygame.sprite.collide_rect(serpiente, comida):
        serpiente.crecer()
        comida.rect.x = random.randint(0, ANCHO_PANTALLA - comida.rect.width)
        comida.rect.y = random.randint(0, ALTO_PANTALLA - comida.rect.height)
        velocidad_actual += INCREMENTO_VELOCIDAD

    # Actualizar la serpiente
    serpiente.update()

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar todos los sprites
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    reloj.tick(15)
