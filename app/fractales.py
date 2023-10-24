import turtle
import fractalartmaker as f
"""
s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("Dibujo de fractales")
#turtle.bgcolor("blue")   # Para cambiar el color de fondo.

t.right(90) # Mover a la derecha
t.forward(100) # Mover hacia delante
t.left(90)    # Mover a la izquierda
t.backward(100)   # Mover hacia atrás
t.goto(100,100)   # Mover a las coordenadas dadas
t.home()        # Mover al origen
t.goto(-100,100)
t.circle(60)    # Para dibujar una circunferencia de ese radio
t.forward(10)
t.dot(10)   # Para dibujar un círculo de ese radio
t.shapesize(3,3,3)   #Para cambiar la apariencia de la torutga. El primer numero es la longitud, el segundo el ancho y el tercero el grosor del borde.
t.pensize(12)   # PAra cambiar el grosor del lápiz
t.fillcolor("red")   # Para cambiar el color de la tortuga
t.forward(100) 
t.pencolor("green")
t.forward(100) # Para cambiara el color del lápiz
t.speed(0.5)    # Cambia la velocidad de la toruga
t.pencolor("black")
t.forward(100)

t.penup()   # Para levantar el lápiz
t.pendown()   # Para bajar el lápiz

t.clear()   #Limpia la pantalla
t.penup()
t.home()
t.pendown()
t.speed(1)
t.forward(300)
t.reset()
t.speed(10)
for i in range(1,10):
    t.circle(10*i)

t.reset()

"""

def koch():
    # Set up Constants
    ANGLES = [60, -120, 60, 0]
    SIZE_OF_SNOWFLAKE = 300
    def get_input_depth():
        """ Obtain input from user and convert to an int"""
        message = 'Please provide the depth (0 or a positive interger):'
        value_as_string = input(message)
        while not value_as_string.isnumeric():
            print('The input must be an integer!')
            value_as_string = input(message)
        return int(value_as_string)
    def setup_screen(title, background='white', screen_size_x=640,
        screen_size_y=320, tracer_size=800):
        print('Set up Screen')
        turtle.title(title)
        turtle.setup(screen_size_x, screen_size_y)
        turtle.hideturtle()
        turtle.penup()
        turtle.backward(240)
        # Batch drawing to the screen for faster rendering
        turtle.tracer(tracer_size)
        turtle.bgcolor(background) # Set the background colour of the screen

    def draw_koch(size, depth):
        if depth > 0:
            for angle in ANGLES:
                draw_koch(size / 3, depth - 1)
                turtle.left(angle)
        else:
            turtle.forward(size)


    depth = get_input_depth()
    setup_screen('Koch Snowflake (depth ' + str(depth) + ')', background='black', screen_size_x=1000, screen_size_y=800)
    # Set foreground colours
    turtle.color('sky blue')
    # Ensure snowflake is centred
    turtle.penup()
    turtle.setposition(-180,0)
    turtle.left(30)
    turtle.pendown()
    turtle.speed(1)
    # Draw three sides of snowflake
    for _ in range(3):
        draw_koch(SIZE_OF_SNOWFLAKE, depth)
        turtle.right(120)
    # Ensure that all the drawing is rendered
    turtle.update()
    print('Done')
    turtle.done()

#koch()
#f.example(1)
f.example(2)
f.example(3)
f.example(4)
f.example(5)
f.example(6)
f.example(7)
f.example(8)
f.example(9)

turtle.mainloop()   # Para que no desaparezca la pantalla