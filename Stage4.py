import pyxel
import Stage
import Enemy1
import Toge

class Stage4(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(0, 88))
        self.enemies.append(Toge.Toge(40, 40))
        self.enemies.append(Toge.Toge(120, 60))
        
        self.collision_tiles = [(61-60, 10),(62-60,10),(63-60,10),(64-60,10),(65-60,10),(66-60,10),(67-60,10),(68-60,10),(69-60,10),(70-60,10),(71-60,10),(72-60,10),(73-60,10),(74-60,10),
        (70-60,9),(71-60,9)
        ]

    def draw(self):
        # pyxel.bltm(0, 0, 0, 0, 0, 160, 120, scale=2.0) # bltm does not support scale
        # Manual scaled draw
        for ty in range(15): # 0 to 14
            for tx in range(20): # 0 to 19
                tile = pyxel.tilemaps[0].pget(tx + 60, ty) # Offset by +60
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
