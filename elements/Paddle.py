from .Draw import Draw


class Paddle(Draw):

    def __init__(self, width=1, height=5):
        super().__init__(width, height)

    def draw(self):
        super().draw()
        self.shape.shapesize(self.width, self.height)

