import pygame
import sys
import numpy as np

# Inicialización de pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 1000, 1000

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Creación de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dibuja lo que quieras ")

# Lista para almacenar los puntos del trazado
points = []

def draw_line(points_list):
    # Dibuja la línea basándose en la lista de puntos recibida
    if len(points_list) > 1:
        pygame.draw.lines(screen, BLACK, False, points_list, 2)

def draw_points(point_list):
        # Dibuja los puntos de la lista en la pantalla
        for point in point_list:
            pygame.draw.circle(screen, (255, 0, 0), point, 3)

def discrete_fourier_transform(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)



def puntos_finales(listapuntos):
    """
        Dibuja en la pantalla los puntos sacados de cuando se dibujó.
    """
    # Dimensiones de la ventana
    WIDTH, HEIGHT = 1000, 1000
    # Colores
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Puntos finales")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar la ventana con el fondo blanco
        screen.fill(WHITE)

        # Dibujar los puntos en la pantalla
        draw_points(listapuntos)

        # Actualizar la ventana
        pygame.display.flip()
    pygame.quit()
    #sys.exit()




def main():
    running = True
    mouse_pressed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Al hacer clic, se activa el flag para guardar coordenadas
                mouse_pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # Al soltar el clic, se desactiva el flag
                mouse_pressed = False

        # Si el botón del ratón está pulsado, se guardan las coordenadas
        if mouse_pressed:
            points.append(pygame.mouse.get_pos())

        # Actualizar la ventana con el fondo blanco
        screen.fill(WHITE)

        # Dibujar la línea con los puntos registrados
        draw_line(points)

        # Actualizar la ventana
        pygame.display.flip()

    print(points)
    print(len(points))
    print(discrete_fourier_transform(points))
    puntos_finales(points)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
