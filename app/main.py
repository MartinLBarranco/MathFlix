import tkinter as tk
import abrefractales
import juegoVida
from collatz import dibujaNHastaUno, dibujaNumIteraciones
from montecarlo import montecarlo as mont
import os
import typer
import tkinter as tk

app = typer.Typer()

@app.command()
def collatznumero(n:int):
    try:
        dibujaNHastaUno(n)
    except Exception as e:
        print(e)

@app.command()
def collatziteraciones(n:int):
    try:
        dibujaNumIteraciones(n)
    except Exception as e:
        print(e)

@app.command()
def juegodelavida():
    juegoVida.juego()

@app.command()
def abre():
    abrefractales.abre()

@app.command()
def montecarlo():
    nombres_archivos = []
    for nombre in os.listdir("app\imagenesmontecarlo"):
        if os.path.isfile(os.path.join("app\imagenesmontecarlo", nombre)):
            nombres_archivos.append(os.path.splitext(nombre)[0])
    print("FIGURAS DISPONIBLES:\n")
    for elem in nombres_archivos:
        print(elem)
    c = input("\nELIGE LA FIGURA: ")
    while c not in nombres_archivos:
        print("\nFiguras disponibles:\n")
        for elem in nombres_archivos:
            print(elem)
        c = input("\nELIGE LA FIGURA:")
    try:
        mont(c)
    except Exception as e:
        print(e)

# -------------------------------------------------------------------------
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("MATHFLIX")

# Configurar la resolución de la ventana
ventana.geometry("600x400")

# Para el juego de la vida y la ventana de los fractales
# Crear un frame para centrar los botones verticalmente
frame_centro = tk.Frame(ventana)
frame_centro.pack(expand=True)

# Crear los botones
boton1 = tk.Button(frame_centro, text="Fractales Aleatorios", command=abre)
boton2 = tk.Button(frame_centro, text="Juego de la Vida de John Conway", command=juegodelavida)

# Ubicar los botones en la ventana
boton1.pack(side=tk.LEFT, padx=10, pady=5)
boton2.pack(side=tk.LEFT, padx=10, pady=5)


# Para ver cuanto tarda un número en llegar hasta 1.
# Crear un frame para centrar los botones verticalmente
def numIterCollatz():
    numero = boton22.get()
    numero = abs(int(numero))
    try:
        dibujaNHastaUno(numero)
    except Exception as e:
        print(e)

frame_medio = tk.Frame(ventana)
frame_medio.pack(expand=True)

# Crear los botones
boton12 = tk.Button(frame_medio, text="Numeros de iteraciones hasta llegar a 1", command=numIterCollatz)
boton22 = tk.Entry(frame_medio, text="Introduce un número")

# Ubicar los botones en la ventana
boton12.pack(side=tk.LEFT, padx=10, pady=5)
boton22.pack(side=tk.LEFT, padx=10, pady=5)



# Para ver las iteraciones de cada numero
# Crear un frame para centrar los botones verticalmente
def numIterCollatzHasta():
    numero = boton23.get()
    numero = abs(int(numero))
    try:
        dibujaNumIteraciones(numero)
    except Exception as e:
        print(e)

frame_abajo = tk.Frame(ventana)
frame_abajo.pack(expand=True)

# Crear los botones
boton13 = tk.Button(frame_abajo, text="Numeros de iteraciones de todos los números hasta", command=numIterCollatzHasta)
boton23 = tk.Entry(frame_abajo, text="Introduce un número")

# Ubicar los botones en la ventana
boton13.pack(side=tk.LEFT, padx=10, pady=5)
boton23.pack(side=tk.LEFT, padx=10, pady=5)


#Para el método montecarlo
nombres_archivos = []
for nombre in os.listdir("app\imagenesmontecarlo"):
    if os.path.isfile(os.path.join("app\imagenesmontecarlo", nombre)):
        nombres_archivos.append(os.path.splitext(nombre)[0])
#print("FIGURAS DISPONIBLES:\n")
#for elem in nombres_archivos:
#   print(elem)

elegido = tk.StringVar()
elegido.set(nombres_archivos[0])

def monte():
    mont(elegido.get())

frame_monte = tk.Frame(ventana)
frame_monte.pack(expand=True)

boton_monte = tk.Button(frame_monte, text="Aplicar método Monte-Carlo", command=monte)
drop = tk.OptionMenu(frame_monte, elegido, *nombres_archivos)

boton_monte.pack(side=tk.LEFT, padx=10, pady=5)
drop.pack(side=tk.LEFT, padx=10, pady=5)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()

# -------------------------------------------------------------------------