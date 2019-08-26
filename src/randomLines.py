import turtle  # turtle
import sys  # argv
import random  # random numbers


def tocenter(heading):
    turtle.color('white')
    turtle.setheading(360-heading)
    turtle.forward(300)

#  not connected, set random x and y
def drawlines3(lines):
    turtle.pendown()

    for i in range(lines):
        turtle.width(random.randint(0, 10))
        turtle.up()
        turtle.setx(random.randint(-300, 300))
        turtle.sety(random.randint(-400, 400))
        turtle.color(COLORS[random.randint(0, 8)])
        turtle.setheading(random.randint(-360, 360))
        turtle.down()
        turtle.forward(random.randint(20, 200))
        turtle.width(random.randint(0, 10))


#  connected, set rand x and y
def drawlines2(lines):
    turtle.pendown()

    for i in range(lines):
        turtle.width(random.randint(0, 10))
        turtle.setx(random.randint(-300, 300))
        turtle.sety(random.randint(-400, 400))
        turtle.color(COLORS[random.randint(0, 8)])
        turtle.setheading(random.randint(-360, 360))
        turtle.forward(random.randint(20, 200))
        turtle.width(random.randint(0, 10))


def drawlines(lines):
    # draws random length and color lines
    # parameters:
    # lines: number of lines to be drawn
    turtle.pendown()

    for i in range(lines):
        turtle.width(random.randint(0, 10))
        heading = random.randint(0,360)
        x = turtle.xcor()
        y = turtle.ycor()
        if x > 300 or x < -300:
            turtle.setx(0)
        if y > 250 or y < -250:
            turtle.sety(0)
        turtle.color(COLORS[random.randint(0, 8)])
        turtle.setheading(heading)
        turtle.forward(random.randint(20,200))


# window dimensions
WINDOW_LENGTH = 800

# Pen Size
UNFILL_PEN_WIDTH = 8

# constants for number of lines and background color
num_lines = 0
background_color = "white"

# color options
COLORS = 'red', 'orange', 'yellow', 'SpringGreen3', 'deep sky blue', 'coral', 'medium purple', 'pink', 'medium slate blue'


def main() -> None:

    turtle.screensize(WINDOW_LENGTH, WINDOW_LENGTH)
    num_lines = int(sys.argv[2])
    background_color = sys.argv[1]

    turtle.width(UNFILL_PEN_WIDTH)
    turtle.tracer(0, 0)
    turtle.bgcolor(background_color)
    print(drawlines(num_lines))

    turtle.update()

    turtle.mainloop()


if __name__ == '__main__':
    main()