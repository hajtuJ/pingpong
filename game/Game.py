

class Game:

    def __init__(self, screen, players):
        self.screen = screen
        self.players = players

    def init(self):
        for player in self.players:
            player.register()

    def loop(self):
        while True:
            self.screen.update()
