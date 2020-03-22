from game.Game import Game

from game.control.Control import Control
from game.control.Controls import Controls

from game.player.Player import Player
from game.player.Players import Players

from elements.Paddle import Paddle

p1up = Control('up', 'w')
p1down = Control('down', 's')
p2up = Control('up', 'o')
p2down = Control('down', 'l')

p1Controls = Controls(p1up, p1down)
p2Controls = Controls(p2up, p2down)

p1Body = Paddle()
p2Body = Paddle()

player1 = Player(p1Body, p1Controls, "Player 1")
player2 = Player(p2Body, p2Controls, "Player 2")

players = Players()
players.add(player1)
players.add(player2)

game = Game(players)
game.init()
