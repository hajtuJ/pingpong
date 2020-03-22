
class Players:

    def __init__(self):
        self.players = []

    def add(self, player):
        self.players.append(player)

    def draw(self, screen):
        for index, player in enumerate(self.players):
            player.draw(screen)
            player.set_init_pos(screen, index == 0)

    # def update(self):


