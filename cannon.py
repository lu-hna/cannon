# Juego de tiro parabólico basado en la colección de FreeGames
# donde se hicieron modificaciones para una mejor experiencia
# de juego.
# Autores: Regina Luna, A01655821
#          Diego Samperio, A01662935
#          Abigail Curiel, A01655892
# Fecha: 23/03/2023

# Se importan las librerías que se utilizarán.
from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Función que responde a un tap en la pantalla.
# Toma como parámetro las coordenadas en x y y de 
# el toque o click en la pantalla.
# No hay valor de retorno.
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199

        # Se disminuye el denominador para
        # incrementar la velocidad de la pelota.
        speed.x = (x + 200) / 11
        speed.y = (y + 200) / 11


# Función que evalúa si una coordenada está
# dentro de la pantalla.
# Toma como parámetro una coordenada de tipo (x,y)
# a evaluar.
# Regresa Verdadero si la coordenada dada está dentro
# de la pantalla, de lo contrario regresa Falso.
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Función que dibuja la pelota y los objetivos.
# No toma parámetros.
# No hay valor de retorno.
def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Función que mueve a la pelota y a los objetivos.
# No toma parámetros.
# No hay valor de retorno.
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Se modifica la velocidad de los objetivos.
    for target in targets:
        target.x -= 4

    # Se modifica la velocidad de la pelota.
    if inside(ball):
        speed.y -= 0.75
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Las bolas reaparecen del otro lado cuando
    # se salen de la pantalla, haciendo al juego
    # infinito.
    for target in targets:
        if not inside(target):
            y = randrange(-150, 150)
            target.x = 190
            target.y = y

    ontimer(move, 20)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
