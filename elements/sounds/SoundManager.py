from .Sound import Sound
from .Sounds import Sounds


sounds = Sounds()
sounds.register(Sound('hit', 'sound/hit.wav'))
sounds.register(Sound('lose', 'sound/lose.wav'))
sounds.register(Sound('win', 'sound/win.wav'))
sounds.register(Sound('startup', 'sound/startup.wav'))
