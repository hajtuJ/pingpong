

class Player:

    def __init__(self, body, controls, name):
        self.body = body
        self.controls = controls
        self.name = name

    def draw(self, screen):
        self.body.draw()
        self.set_init_pos(screen)

    def set_init_pos(self, screen, right=True):
        half_width = screen.wn.screensize()[0]
        if right:
            self.body.setpos(half_width - self.body.width / 2, 0)
        else:
            self.body.setpos(-half_width + self.body.width / 2, 0)
