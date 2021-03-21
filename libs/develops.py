import turtle

# ---------------------------------#


def detect_progress(item: tuple) -> tuple:
    key, value = item
    dx = 0
    dy = 0

    if key == "1":
        dx = 0
        dy = value

    if key == "2":
        dx = value
        dy = value

    if key == "3":
        dx = value
        dy = 0

    if key == "4":
        dx = value
        dy = -1 * value

    if key == "5":
        dx = 0
        dy = -1 * value

    if key == "6":
        dx = -1 * value
        dy = -1 * value

    if key == "7":
        dx = -1 * value
        dy = 0

    if key == "8":
        dx = -1 * value
        dy = value

    return dx, dy
# ---------------------------------#


def draw_points(t: turtle.Turtle, points: dict, step: int) -> None:

    t.speed()
    t.color('red')
    t.pensize(2)
    x, y, i = 0, 0, 0

    for item in points:
        i += 1
        x, y = item
        t.color('red')
        t.setposition(x * step, y * step)
        t.color('blue')
        t.circle(1)
        t.color('green')
        t.write(i)

    t.up()
    t.setposition(x * step, y * step - 20)
    t.down()
    t.write('x:'+str(x)+' y:'+str(y))
    t.up()
    t.setposition(x * step, y * step)
    t.down()
    t.color('blue')
    t.pensize(2)
    t.setposition(0, 0)
# ---------------------------------#

# ---------------------------------#


def create_point(steps: dict) -> dict:
    x = 0
    y = 0
    req = []
    for item in steps:
        dx, dy = detect_progress(item)
        x = x + dx
        y = y + dy
        req.append((x, y))
    return req
# ---------------------------------#
