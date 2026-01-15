import pyxel
import Enemy

class Enemy1(Enemy.Enemy):
    #x: 敵の初期X座標, y: 敵の初期Y座標, min_x: 敵の最小X座標, max_x: 敵の最大X座標
    def __init__(self, x, y, min_x=0, max_x=144):
        super().__init__(x, y, 1)#初期位置x,y,HP
        self.vx = 1
        self.min_x = min_x
        self.max_x = max_x
        self.size = 4
        self.color = 8
        self.deathEffectTime = 0

    def update(self, player):
        if self.hp <= 0:
            self.deathEffectTime += 1
            self.update_effects()
            return 

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
            
            if self.hit_timer > 0:
                for i in range(1, 16):
                    pyxel.pal(i, 7) # Change all non-transparent colors to white(7)
                
            pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 48, w, 16, 0, scale=2.0)
            
            if self.hit_timer > 0:
                pyxel.pal() # Reset palette
        elif self.deathEffectTime < 30:
             u = (self.deathEffectTime // 10) * 16 + 32
             pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 48, 16, 16, 0, scale=2.0)
        
        self.draw_effects()
           