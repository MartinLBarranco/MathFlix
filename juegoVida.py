from sys import exit
import pygame as p
import numpy as np
from time import sleep
from random import randint

"""
Listado de teclas:
    Espacio: Pausar el juego
    r: reiniciar malla
    1: Estáticos
    2: Osciladores
    3: pájaro
    4: crecimiento infinito 1
    5: pistola
    6: aleatorio
    7: crecimiento infinito 2
    8: configuración convergente en mucho tiempo
"""

def juego():
    p.init()
    height, width = 1000,1000
    screen = p.display.set_mode((width +500,height))

    bg = 25,25,25
    screen.fill(bg)

    nxC, nyC = 100, 100   #Numero de celdas en cada eje

    dimCH = height/nxC  #Dimension de la altura de las celdas
    dimCW = width/nyC   #Dimension de la anchura de la celda
    """
    LOGICA:
    1 = vicva
    0 = muerta
    """

    #dibujar matriz de ceros y unos
    def dibujaMatriz(matriz, cord_ini, matrizJuego):
        nFilas, nColumnas = len(matriz), len(matriz[0])
        x0, y0 = cord_ini[0], cord_ini[1]
        for fila in range(0,nFilas):
            for columna in range(0,nColumnas):
                matrizJuego[x0+fila,y0+columna] = matriz[fila][columna]
    """
    CONFIGURACIONES PREESTABLECIDAS
    """

    #ESTÁTICAS

    #Su coordenada inical va a ser (20,50)
    ovalo = [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]

    #Su coordenada inical va a ser (40,50)
    triangulo_girao = [[0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 0, 1],
                    [0, 0, 1, 0]]
    #Su coordenada inical va a ser (60,50)
    cosa_estatica = [[1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]]
    #Su coordenada inical va a ser (80,50)
    cuadrado = [[1,1],
                [1,1]]

    #OSCILADORES
    #Posicion inicial [75,50]
    pulsar = np.zeros((17, 17))
    pulsar[2, 4:7] = 1
    pulsar[4:7, 7] = 1
    pulsar += pulsar.T
    pulsar += pulsar[:, ::-1]
    pulsar += pulsar[::-1, :]
    #Posicion inicial [25,50]
    champiñon = [[1, 1, 1, 0],
                [0, 1, 1, 1]]
    #Posicion inicial [50,50]
    palo = [[1, 1, 1]]


    #PÁJARO
    pajaro = [[1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]]

    #CRECIMINETO INFINITO
    infinito = [[1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1]]
    r_pentomino = [[0, 1, 1],
                [1, 1, 0],
                [0, 1, 0]]

    #PISTOLA
    pistola = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    #CONVERGENTES
    acorn = [[0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1]]

    gameState = np.zeros((nxC,nyC))

    #palo
    gameState[5,3] = 1
    gameState[5,4] = 1
    gameState[5,5] = 1

    #cosa qie se mueve
    gameState[21,21] = 1
    gameState[22,22] = 1
    gameState[22,23] = 1
    gameState[21,23] = 1
    gameState[20,23] = 1

    pausa = False
    nVivas = 0
    generacion = 0

    fuente = p.font.SysFont("segoe print", 50)                                  #Fuente para el título
    fuente2 = p.font.SysFont("segoe print",30)                                  #Fuente para texto

    texto = fuente.render("El juego de la vida", True, (255,255,255))           #Texto de título
    #txtReset = fuente2.render("Reset", True, (255,255,255), (107, 119, 138))

    button_rect = p.Rect(1300, 200, 75, 25)

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit() #exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE:      #Se comprueba si la tecla del espacio se ha pulsado para pausar el juego
                    pausa = not pausa
                if event.key == p.K_r:          #Se comprueba si la tecla r se ha pulsado para reiniciar el juego
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                if event.key == p.K_1:          #Se comprueba si se ha pulsado la tecla 1
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(ovalo, [20,50], gameState)
                    dibujaMatriz(triangulo_girao, [40,50], gameState)
                    dibujaMatriz(cosa_estatica, [60,50], gameState)
                    dibujaMatriz(cuadrado, [80,50], gameState)
                if event.key == p.K_2:          #Se comprueba si se ha pulsado la tecla 2
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(palo, [25,50], gameState)
                    dibujaMatriz(champiñon, [50,50], gameState)
                    dibujaMatriz(pulsar, [75,42], gameState)
                if event.key == p.K_3:          #Se comprueba si se ha pulsado la tecla 3
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(pajaro, [10,10], gameState)
                if event.key == p.K_4:          #Se comprueba si se ha pulsado la tecla 4
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(infinito, [47,50], gameState)
                if event.key == p.K_5:          #Se comprueba si se ha pulsado la tecla 5
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(pistola, [10,10], gameState)
                if event.key == p.K_6:          #Se comprueba si se ha pulsado la tecla 5
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    for i in range(0,nxC):
                        for j in range(0,nyC):
                            gameState[i,j] = randint(0,1)
                if event.key == p.K_7:          #Se comprueba si se ha pulsado la tecla 5
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(r_pentomino, [50,50], gameState)
                if event.key == p.K_8:          #Se comprueba si se ha pulsado la tecla 5
                    gameState = np.zeros((nxC,nyC))
                    generacion = 0
                    dibujaMatriz(acorn, [50,50], gameState)

        newGameState = np.copy(gameState)
        screen.fill(bg)
        sleep(0.03)  #delay para darle una pausita para que descanse
    
        if p.mouse.get_pressed()[0]:            #Si se clica el boton izquierdo sobre una celda viva, se mata, y viceversa.
            (posX, posY) = p.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            #print(celX,celY)
            if celX <= nxC and celY <= nyC:
                if newGameState[celX, celY] == 1:
                    newGameState[celX, celY] = 0
                else:
                    newGameState[celX, celY] = 1

        for y in range(0,nxC):
            for x in range(0,nyC):
                if pausa:                                                           #Comprueba si el juego está pausado
                    n_vecinos = gameState[(x-1) % nxC, (y-1) % nyC] + \
                                gameState[(x) % nxC, (y-1) % nyC] + \
                                gameState[(x+1) % nxC, (y-1) % nyC] + \
                                gameState[(x-1) % nxC, (y) % nyC] + \
                                gameState[(x+1) % nxC, (y) % nyC] + \
                                gameState[(x-1) % nxC, (y+1) % nyC] + \
                                gameState[(x) % nxC, (y+1) % nyC] + \
                                gameState[(x+1) % nxC, (y+1) % nyC]
                    
                    if gameState[x,y] == 0 and n_vecinos == 3:                      #REGLA 1
                        newGameState[x,y] = 1
                    elif gameState[x,y] == 1 and (n_vecinos < 2 or n_vecinos > 3):  #REGLA 2
                        newGameState[x,y] = 0

                poly = [((x)*dimCW, (y)*dimCH),                                     #polígono que dibuja la celda
                        ((x+1)*dimCW, (y)*dimCH),
                        ((x+1)*dimCW, (y+1)*dimCH),
                        ((x)*dimCW, (y+1)*dimCH)]
                
                if newGameState[x,y] == 0:                                          #Se dibujan las celdas negras
                    p.draw.polygon(screen, (128,128,128), poly,1)
                else:                                                               #Se dibujan las celdas blancas
                    p.draw.polygon(screen, (255,255,255), poly,0)
        
        gameState = np.copy(newGameState)
        
        nVivas = int(gameState.sum())

        screen.blit(texto, (1100,25))       #Se añade el texto de título
        
        txtVivas = fuente2.render("Celdas vivas: " + str(nVivas), True, (255,255,255))              #Como este texto se va cambiadno, ha de estar dentro del bucle
        txtGeneracion = fuente2.render("Generación: " + str(generacion), True, (255,255,255))
        
        screen.blit(txtVivas,(1010,200))                                                            #Se renderiza el texto
        screen.blit(txtGeneracion,(1010,270))
        if pausa:
            generacion += 1
        
        p.display.flip()            #Siguiente frame

