import pyxel
import Player
import Enemy1

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.load("my_resource.pyxres")
        self.player = Player.Player()   
        self.enemy1 = Enemy1.Enemy1(50, 80)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.enemy1.update()
        self.enemy1.Damage(self.player.bullets)
        self.player.Damage(self.enemy1)
        
        

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        self.enemy1.draw()

App()
