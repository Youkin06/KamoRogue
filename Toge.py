import pyxel
import Enemy

class Toge(Enemy.Enemy):
    def __init__(self, x, y, detection_range_tile=2):
        super().__init__(x, y, 1) # HP=1
        self.initial_y = y
        self.is_falling = False
        self.fall_speed = 4
        self.u = 8
        self.v = 16
        # 下なんマスまでか
        self.detection_range_tile = detection_range_tile
        
        # Hitbox override
        self.hitbox_offset_x = -2
        self.hitbox_offset_y = -2
        self.hitbox_width = 8
        self.hitbox_height = 8
        
    def update(self, player):
        if self.hp <= 0:
            return

        if not self.is_falling:
            # Detection logic
            # Toge is 8x8. Center is x + 4.
            # Player is 16x16. Center is x + 8.
            
            my_cx = self.x + 2
            player_cx = player.x + 8
            
            # X Detection: 
            # 8px width.
            if abs(my_cx - player_cx) < 6: 
                # Y Detection: Use detection_range_tile * 8 (pixels per tile)
                dist_y = player.y - (self.y + 8)
                if 0 <= dist_y <= self.detection_range_tile * 8:
                     self.is_falling = True
        else:
            self.y += self.fall_speed
            
            # Remove if falls off screen (assumed bottom is 240)
            if self.y > 240:
                self.hp = 0
            
        super().update_effects()

    def draw(self):
        if self.hp > 0:
            pyxel.blt(self.x * 2, self.y * 2, 1, self.u, self.v, 8, 8, 0, scale=2.0)
            
            # Debug lines removed
            pass
        
        self.draw_effects()
