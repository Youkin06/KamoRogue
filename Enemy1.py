import pyxel
import Enemy

class Enemy1(Enemy.Enemy):
    def __init__(self, x, y, min_x=0, max_x=144):
        super().__init__(x, y, 10)#初期位置x,y,HP
        self.vx = 1
        self.min_x = min_x
        self.max_x = max_x
        self.size = 4
        self.color = 8 

    def update(self, player):
        if self.hp > 0:
            self.x += self.vx
            
            if self.x < self.min_x:
                self.x = self.min_x
                self.vx *= -1
            if self.x > self.max_x:
                self.x = self.max_x
                self.vx *= -1
            
            super().update(player)
    
    def draw(self):
        if self.hp > 0:
            u = (pyxel.frame_count // 6 % 2) * 16
            w = 16
            if self.vx > 0:
                w = -16
            else:
                w = 16
            
            pyxel.blt(self.x, self.y, 0, u, 48, w, 16, 0)
           