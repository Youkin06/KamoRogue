import pyxel
import Enemy

class Enemy1(Enemy.Enemy):
    def __init__(self, x, y):
        super().__init__(x, y, 10)
        self.vx = 1
        self.size = 4
        self.color = 8 

    def update(self, player):
        if self.hp > 0:
            self.x += self.vx
            
            if self.x < 0:
                self.x = 0
                self.vx *= -1
            if self.x > 160 - 16:
                self.x = 160 - 16
                self.vx *= -1
            
            super().update_common(player)
    
    def draw(self):
        if self.hp > 0:
            u = (pyxel.frame_count // 6 % 2) * 16
            w = 16
            if self.vx > 0:
                w = -16
            else:
                w = 16
            
            pyxel.blt(self.x, self.y, 0, u, 48, w, 16, 0)
           