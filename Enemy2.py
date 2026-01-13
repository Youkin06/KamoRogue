import pyxel
import Enemy

class Enemy2(Enemy.Enemy):
    def __init__(self, x, y, min_x=0, max_x=144):
        super().__init__(x, y, 10)#初期位置x,y,HP
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
                
            # Changed source Y (v) to 128 as requested
            pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 128, w, 16, 0, scale=2.0)
            
            if self.hit_timer > 0:
                pyxel.pal() # Reset palette
        elif self.deathEffectTime < 30:
             u = (self.deathEffectTime // 10) * 16 + 32
             # Note: User said "same as death animation", so I assume death effect source Y is also 48? 
             # "死んだ時のアニメーション、idle全て同じです。y軸のみ違います。y座標を128にしてください。"
             # "y-axis ONLY is different. Please set y-coordinate to 128."
             # Does this apply to death effect too?
             # Death effect sprite is at 48 in Enemy1. 
             # If "everything is same except y-axis", technically death animation might also need to be at 128 if the sprite sheet is arranged that way.
             # However, common sense suggests death effect might be shared.
             # BUT, user said "set y-coordinate to 128".
             # Let's assume the sprite sheet has a full set of Enemy2 sprites at y=128.
             # So I will change this to 128 as well.
             pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 128, 16, 16, 0, scale=2.0)
        
        self.draw_effects()
