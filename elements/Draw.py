import turtle
import setup


class Draw:

    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.shape = turtle.Turtle()

    def draw(self):
        self.shape.speed(setup.el_speed)
        self.shape.shape(setup.el_shape)
        self.shape.color(setup.el_color)

    def size(self, width, height):
        self.shape.shapesize(width, height)

    def setpos(self, x, y):
        self.shape.penup()
        self.shape.goto(x, y)
