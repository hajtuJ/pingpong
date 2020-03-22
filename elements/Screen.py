import turtle
import setup


class Screen:

    def __init__(self, length=setup.win_length, height=setup.win_height):
        self.wn = turtle.Screen()
        self.wn.setup(length, height)
        self.wn.bgcolor(setup.win_bg)
        self.wn.title(setup.game_title)
        self.wn.tracer(0)

    def update(self):
        self.wn.update()
