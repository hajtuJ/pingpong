import pyglet

pyglet.options['audio'] = ('openal', 'silent')


class Sound:

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def play(self):
        sound = pyglet.media.load(self.path, streaming=False)
        sound.play()
