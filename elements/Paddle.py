from .Draw import Draw


class Paddle(Draw):

    def __init__(self, width=30, height=5):
        width = width
        height = height
        super().__init__(width/10, height/10)

    def draw(self):
        super().draw()
        self.shape.shapesize(self.width, self.height)
