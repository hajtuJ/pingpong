from elements.Screen import Screen


class Game:

    def __init__(self, players):
        self.screen = Screen()
        self.players = players

    def init(self):
        self.screen.update()
        self.players.draw(self.screen)
        self.loop()

    def loop(self):
        while True:
            self.screen.update()
            # self.players.update()
