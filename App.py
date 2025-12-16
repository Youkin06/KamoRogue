import pyxel
import Player
import Enemy1

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.load("my_resource.pyxres")
        self.player = Player.Player()   
        self.enemies = []
        self.enemies.append(Enemy1.Enemy1(50, 80))
        # self.enemies.append(Enemy1.Enemy1(100, 80))
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update(self.player)
            enemy.Damage(self.player.bullets)
        
        self.player.Damage(self.enemies)
        

    def draw(self):
        pyxel.cls(0)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()

App()
