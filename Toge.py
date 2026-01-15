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
        
    def update(self, player):
        if self.hp <= 0:
            return

        if not self.is_falling:
            # Detection logic
            # Player is below and within horizontal range
            # Toge width 16, Player width 16. check overlap.
            
            # center x
            my_cx = self.x + 8
            player_cx = player.x + 8
            
            if abs(my_cx - player_cx) < 12: # Check horizontal alignment approx
                # Check vertical
                # Player should be below (player.y > self.y)
                # And within 2 tiles (16px) distance? "下に2マスまでしか検知しない"
                # so distance < 32 (16 height of Toge + 16 gap + 16 player height?)
                # Interpreting "within 2 tiles below": distance from bottom of Toge to top of Player is <= 16
                
                dist_y = player.y - (self.y + 16)
                if 0 <= dist_y <= 16:
                     self.is_falling = True
        else:
            self.y += self.fall_speed
            
            # Simple floor/out of bounds check could be added, but user didn't request.
            # It will just keep falling forever or until hit.
            
        super().update_effects()

    def draw(self):
        if self.hp > 0:
            pyxel.blt(self.x * 2, self.y * 2, 1, self.u, self.v, 16, 16, 0, scale=2.0)
        
        self.draw_effects()
