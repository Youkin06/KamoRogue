import pyxel
import Player

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.load("my_resource.pyxres")
        self.player = Player.Player()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        

    def draw(self):
        pyxel.cls(0)
        self.player.draw()

App()
