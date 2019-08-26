import turtle  # turtle
import sys  # argv
from PIL import Image
import cv2
import random  # random numbers

# window dimensions
WINDOW_LENGTH = 600

# Pen Size
UNFILL_PEN_WIDTH = 8

# constants for number of lines and background color
num_lines = 0
background_color = "white"

def draw_image(name):
    f = Image.open(name, 'r')
    img = f.load()
    turtle.screensize(f.size(), f.size())
    total = 0
    dim = f.size() * f.size()
    while total < dim :
            x
            [r, g, b] = img[x, y]
            fd = random.randint(0, 20)
            total += fd
            turtle.pencolor(r, g, b)
            turtle.setHeading(random.randint(-360, 360))
            turtle.fd(fd);
            turtle.pendown


def main() -> None:

    turtle.screensize(WINDOW_LENGTH, WINDOW_LENGTH)
    name = sys.argv[1]

    turtle.width(UNFILL_PEN_WIDTH)
    turtle.tracer(0, 0)
    turtle.bgcolor(background_color)
    #print(draw_image(name))
    turtle.penup()
    turtle.setx(-300)
    turtle.sety(300)
    turtle.pendown()
    turtle.forward(50)
    turtle.update()

    turtle.mainloop()


if __name__ == '__main__':
    main()