import pyxel
import Stage
import Enemy1
import Enemy3
import Enemy2
import Toge

class Stage5(Stage.Stage):
    def __init__(self):
        super().__init__()
        # Use Stage4 settings or defaults as a base. User didn't specify content for Stage5.
        # I'll make it simple for now.
        
        self.limit_x_min = 0 # Default
        self.limit_x_max = 144 # Default
        
        self.player_start_x = 16
        self.player_start_y = 88
        
        # Add some default collision tiles or just leave empty/minimal
        self.collision_tiles = [] 
        
        # Add a dummy enemy for now? Or leave empty? 
        # Usually having 1 enemy is good for testing "clear" logic, 
        # but user just asked to "create Stage5".
        # I'll add one simple enemy.
        self.enemies.append(Enemy3.Enemy3(100, 88, 80, 120))

    def draw(self):
        # reuse Stage1/Test draw logic (tilemap)
        for ty in range(15): 
            for tx in range(20): 
                tile = pyxel.tilemaps[0].pget(tx + 80, ty) # Offset by +80
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
