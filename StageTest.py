import pyxel
import Stage
import Enemy1

class StageTest(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(50, 80))
        self.enemies.append(Enemy1.Enemy1(150, 80, 100, 150))

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
        super().draw()
