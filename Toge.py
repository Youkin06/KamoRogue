import pyxel
import Enemy

class Toge(Enemy.Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 1) # HP=1
        self.initial_y = y
        self.is_falling = False
        self.fall_speed = 4
        self.u = 8
        self.v = 16
        # 下なんマスまでか
        self.detection_range_tile = 8
        
        # Hitbox override
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
                # Y Detection: 3 tiles (24px)
                dist_y = player.y - (self.y + 8)
                if 0 <= dist_y <= 24: # 3 tiles
                     self.is_falling = True
        else:
            self.y += self.fall_speed
            
            # Simple floor/out of bounds check could be added, but user didn't request.
            # It will just keep falling forever or until hit.
            
        super().update_effects()

    def draw(self):
        if self.hp > 0:
            pyxel.blt(self.x * 2, self.y * 2, 1, self.u, self.v, 8, 8, 0, scale=2.0)
            
            # Debug: Draw Hitbox (Red)
            hx = (self.x + self.hitbox_offset_x) * 2
            hy = (self.y + self.hitbox_offset_y) * 2
            hw = self.hitbox_width * 2
            hh = self.hitbox_height * 2
            pyxel.rectb(hx, hy, hw, hh, 8) # 8 = Red
            
            # Debug: Draw Detection Range (Yellow)
            range_x = (self.x + 2 - 6) * 2 
            range_y = (self.y + 8) * 2
            range_w = (6 * 2) * 2
            range_h = 24 * 2
            
            pyxel.rectb(range_x, range_y, range_w, range_h, 10) # 10 = Yellow
        
        self.draw_effects()
