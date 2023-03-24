"""Memory, puzzle game of number pairs.
Arturo Ordoñez Jarillo 
Daniel de la Peña Rosales 
"""

from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
num_taps = 0  # initialize tap count to 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def colores(mem):
    if (mem >= 0 and mem <= 4):
        return 'blue4'
    elif (mem >= 5 and mem <= 8):
        return 'DarkRed'
    elif (mem >= 9 and mem <= 12):
        return 'chocolate4'
    elif (mem >= 13 and mem <= 16):
        return 'DarkGreen'
    elif (mem >= 17 and mem <= 20):
        return 'purple'
    elif (mem >= 21 and mem <= 24):
        return 'orange'
    elif (mem >= 25 and mem <= 28):
        return 'DarkSlateBlue'
    elif (mem >= 29 and mem <= 32):
        return 'black'

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global num_taps  # reference the global variable
    num_taps += 1  # increment the tap count
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y)
        color(colores(tiles[mark]))
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center")


    # display the number of taps
    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {num_taps}', font=('Arial', 16, 'normal'))

    # check if all squares have been uncovered
    if all(not h for h in hide):
        up()
        goto(0, 0)
        color('black')
        write("Congratulations! You've uncovered all squares!", align="center",
              font=('Arial', 15, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()