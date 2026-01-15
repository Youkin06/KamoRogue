import pyxel
import Stage
import Enemy1

class Stage2(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(0, 88))
        #self.enemies.append(Enemy1.Enemy1(150, 88, 0, 150))
        # Platform 1: Tiles (5,6) to (7,6)
        # x range: 5*8=40 to (7+1)*8 - 16 = 48
        # y: 6*8 - 16 = 32
        self.enemies.append(Enemy1.Enemy1(5 * 8, 6 * 8 - 16, 5*8 , 5*8 + 8))

        # Platform 2: Tiles (9,10) to (12,10)
        # x range: 9*8=72 to (12+1)*8 - 16 = 88
        # y: 10*8 - 16 = 64
        self.enemies.append(Enemy1.Enemy1(12 * 8, 6 * 8 - 16, 12*8+8 , 17*8-8))
        self.collision_tiles = [(5,6),(6,6),(7,6),(9,10),(10,10),(11,10),(12,10),(14,6),(15,6),(16,6),(17,6)]

    def draw(self):
        # pyxel.bltm(0, 0, 0, 0, 0, 160, 120, scale=2.0) # bltm does not support scale
        # Manual scaled draw
        for ty in range(15): # 0 to 14
            for tx in range(20): # 0 to 19
                tile = pyxel.tilemaps[0].pget(tx + 20, ty) # Offset by +20
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
