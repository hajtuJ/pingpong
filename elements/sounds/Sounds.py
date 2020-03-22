

class Sounds:

    def __init__(self):
        self.sounds = {}

    def register(self, sound):
        if sound.name not in self.sounds:
            self.sounds[sound.name] = sound

    def play(self, name):
        self.sounds[name].play()
