import pyxel
import Stage
import Enemy1
import Enemy2

class Stage3(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.player_start_x = 1 * 16
        self.player_start_y = 12 * 16
        #self.enemies.append(Enemy1.Enemy1(0, 88, 0, 6 * 8 -16))
        self.enemies.append(Enemy2.Enemy2(8* 10 + 16, 88, 8* 10 +8, 15* 12 - 32))
        self.enemies.append(Enemy2.Enemy2(2 * 8, 9* 7 -8, 2*8, 4*8))
        
        self.collision_tiles = [(2,9),(3,9),(4,9),(6,12),(7,12),(8,12),(9,12),(10,12),(13,7),(14,7),(15,7)]

    def draw(self):
        # pyxel.bltm(0, 0, 0, 0, 0, 160, 120, scale=2.0) # bltm does not support scale
        # 手動スケーリング描画
        for ty in range(15): # 0 to 14
            for tx in range(20): # 0 to 19
                tile = pyxel.tilemaps[0].pget(tx + 40, ty) # +40オフセット
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
