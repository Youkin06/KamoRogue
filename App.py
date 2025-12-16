import pyxel
import Player
import StageTest

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.load("my_resource.pyxres")
        self.player = Player.Player()   
        self.stage = StageTest.StageTest()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.stage.update(self.player)
        
        self.player.Damage(self.stage.enemies)
        

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.stage.draw()

App()
