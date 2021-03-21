import turtle

# *******************
# drawing a square x,y - coordonates, a measure of base#
def sq(x:int, y:int, a:int )->None:
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
# ******************* #

# *******************
# create grid, axex an inscriptions,
# n - count of squere in a cadran, a - measure of one squere#
def draw_grid(n:int, a:int)->None:


    turtle.tracer(False)
    turtle.color('silver')
    y = -1 * n * a
    for i in range(n*2):
        x = -1 * (n+1) * a
        for j in range(n*2):
            x = x + a
            sq (x, y, a)
        y = y + a

    turtle.up()
    turtle.setposition(0, 0)
    turtle.down()
    turtle.color('black')
    turtle.pensize(2)

    turtle.up()
    turtle.setposition(-1 * n * a, 0)
    turtle.down()
    turtle.forward(2 * n * a)
    for i in range(2*n+1):
        turtle.up()
        turtle.setposition(-1 * (n-i) * a, 5)
        turtle.down()
        if i != n:
            turtle.write((-1*n)+i, move=False, font=("Arial", 8, "bold"))

    turtle.up()
    turtle.setposition(0, -1 * n * a)
    turtle.down()
    turtle.left(90)
    turtle.forward(2 * n * a)
    turtle.up()
    turtle.setposition(0, -1 * n * a)
    turtle.down()
    for i in range(2 * n+1):
        turtle.up()
        turtle.setposition(-20, -1 * (n-i) * a)
        turtle.down()
        if i != n:
            turtle.write((-1 * n) + i, move=False, font=("Arial", 8, "bold"))
    turtle.up()
    turtle.setposition(0, 0)
    turtle.left(270)
    turtle.down()

    turtle.tracer(True)
# ******************* #