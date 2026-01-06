import pyxel
import Stage
import Enemy1

class StageTest(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(0, 88))
        self.enemies.append(Enemy1.Enemy1(150, 88, 0, 150))
        
        # Add collision tiles
        self.collision_tiles = [(4, 10), (5, 10), (6, 10), (7, 10),(12,5),(13,5),(14,5),(15,5)]

    def draw(self):
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
        super().draw()
