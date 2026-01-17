import pyxel
import Stage
import Enemy1
import Enemy2

class Stage1(Stage.Stage):
    def __init__(self):
        super().__init__()
        self.player_start_x = 1 * 16
        self.player_start_y = 12 * 16
        
        self.enemies.append(Enemy1.Enemy1(100, 88, 32, 150-8))
        #self.enemies.append(Enemy1.Enemy1(150, 88, 0, 150))
        #self.enemies.append(Enemy2.Enemy2(150, 88, 0, 150))
        
        # 衝突タイルを追加
        self.collision_tiles = [(4, 10), (5, 10), (6, 10), (7, 10)]

    def draw(self):
        # pyxel.bltm(0, 0, 0, 0, 0, 160, 120, scale=2.0) # bltm does not support scale
        # 手動スケーリング描画
        for ty in range(15): # 0 to 14
            for tx in range(20): # 0 to 19
                tile = pyxel.tilemaps[0].pget(tx, ty)
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
