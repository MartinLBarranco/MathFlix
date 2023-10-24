import pygame
import random
import matplotlib.pyplot as plt


def montecarlo(nombreimagen):
    url = ".\\imagenesmontecarlo\\" + nombreimagen + ".png"
    
    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la ventana
    width, height = 960, 720

    # Crear la ventana
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulación Montecarlo")

    # Cargar la imagen de la figura
    figure_image = pygame.image.load(url)

    # Calcular el área de la imagen
    image_area = figure_image.get_width() * figure_image.get_height()

    # Función para comprobar si un punto está dentro de la figura
    def is_point_inside_figure(point):
        # Obtener el color del píxel en las coordenadas del punto
        pixel_color = figure_image.get_at(point)
        
        # Comprobar si el píxel es transparente
        return pixel_color[3] > 0

    # Calcular el área de la figura
    figure_area = sum(1 for y in range(figure_image.get_height()) for x in range(figure_image.get_width()) if is_point_inside_figure((x, y)))

    # Calcular el área de un píxel
    pixel_area = (width * height) / (figure_image.get_width() * figure_image.get_height())

    # Función para seleccionar un punto aleatorio dentro de la ventana
    def get_random_point():
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        return x, y

    def dibuja(valores, area_real, puntos_dentro_d, puntos_fuera_d):
        """
            Output: La gráfica que muestra la evolución de la aproximación del área
        """
        # Crear una lista de índices para el eje x
        indices = range(len(valores))
        
        # Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(15,10))
        
        # Trazar los valores de la lista
        ax.plot(indices, valores, label="Área aproximada.")
        
        # Trazar la línea constante
        ax.axhline(y=area_real, color='r', linestyle='--', label='Área real de la figura')
        
        # Personalizar el gráfico
        #ax.set_xlabel('')
        ax.set_ylabel('Área en píxeles al cuadrado')
        ax.set_title('Evolución del área aproximada')
        ax.legend()
        
        # Añadir el texto en la gráfica
        texto = f'Puntos dentro: {puntos_dentro_d}\nPuntos fuera: {puntos_fuera_d}\nPuntos totales: {puntos_dentro_d+puntos_fuera_d}'
        ax.text(0.9, 0.1, texto, transform=ax.transAxes, verticalalignment='top')
        #x = 0.05
        #y = 0.95
        
        # Mostrar la gráfica
        plt.show()

    # Variables que manejan los puntos que se colocan.
    puntos_dibujados = []
    puntos_dentro = 0
    puntos_fuera = 0
    sucesion_cociente_dentro_vs_total = []

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        
        # Limpiar la ventana
        window.fill((255, 255, 255))
        
        # Dibujar la figura en la ventana
        window.blit(figure_image, (0, 0))

        # Dibujar todos los puntos almacenados en la lista
        for point, color in puntos_dibujados:
            pygame.draw.circle(window, color, point, 5)
        
        # Seleccionar un punto aleatorio dentro de la ventana
        random_point = get_random_point()

        # Comprobar si el punto está dentro de la figura
        if is_point_inside_figure(random_point):
            point_color = (255, 0, 0)  # Color rojo si está dentro
        else:
            point_color = (0, 0, 255)  # Color azul si está fuera
        
        # Comprobar si el punto está dentro de la figura
        if is_point_inside_figure(random_point):
            #print("El punto está dentro de la figura")
            puntos_dentro += 1
        else:
            #print("El punto está fuera de la figura")
            puntos_fuera += 1
        
        # Creamos el siguiente término de la sucesión (num puntos interiores)/(num puntos totales)
        sucesion_cociente_dentro_vs_total.append((puntos_dentro*image_area)/(puntos_dentro + puntos_fuera))

        # Agregar el punto a la lista de puntos dibujados
        puntos_dibujados.append((random_point, point_color))
        
        # Dibujar el punto en la ventana
        pygame.draw.circle(window, point_color, random_point, 1)

        # Actualizar la ventana
        pygame.display.flip()

    # Finalizar Pygame
    pygame.quit()

    dibuja(sucesion_cociente_dentro_vs_total, figure_area, puntos_dentro, puntos_fuera)