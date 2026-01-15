import pyxel
import Stage
import Enemy1
import Toge

class Stage4(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemy1.Enemy1(60, 88, 60, 150-8))
        #self.enemies.append(Toge.Toge(40, 40))
        self.enemies.append(Toge.Toge(120, 60))
        
        self.player_start_x = 16
        self.player_start_y = 88
        self.floor_y = 240
        
        self.collision_tiles = [(61-60, 10),(62-60,10),(63-60,10),(64-60,10),(65-60,10),(66-60,10),(67-60,10),(68-60,10),(69-60,10),(70-60,10),(71-60,10),(72-60,10),(73-60,10),(74-60,10),
        (70-60,9),(71-60,9),
        (65-60,6),(66-60,6),(67-60,6),(68-60,6),(69-60,6),(70-60,6),(71-60,6),(72-60,6),(73-60,6),(74-60,6),(75-60,6),(76-60,6),(77-60,6),
        (65-60,7),(66-60,7),
        (63-60,3),(64-60,3),(65-60,3),(66-60,3),(67-60,3),(68-60,3),(69-60,3),(70-60,3),(71-60,3),
        (60-60,0),(61-60,0),(62-60,0),(63-60,0),(64-60,0),(65-60,0),(66-60,0),(67-60,0),(68-60,0),(69-60,0),(70-60,0),(71-60,0),(72-60,0),(73-60,0),(74-60,0),(75-60,0),(76-60,0),(77-60,0),(78-60,0),
        (63-60,1),(64-60,1),(63-60,2),(64-60,2)
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
