import pyxel
import Stage
import Enemy1

class Stage2(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(0, 88))
        #self.enemies.append(Enemy1.Enemy1(150, 88, 0, 150))
        
        self.collision_tiles = [(4, 10), (5, 10), (6, 10), (7, 10),(12,5),(13,5),(14,5),(15,5)]

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
