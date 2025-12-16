import pyxel

class Enemy:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.vx = 0
        self.knockback_vx = 0
        self.color = 8

    def update(self, player):
        # Knockback Physics
        self.x += self.knockback_vx
        self.knockback_vx *= 0.9
        if abs(self.knockback_vx) < 0.1:
            self.knockback_vx = 0

        # Guard Collision
        if player.guarding and self.knockback_vx == 0:
            gx = player.x
            gy = player.y
            gw = 8
            gh = 16
            
            if player.facingLeft:
                gx = player.x - 7
            else:
                gx = player.x + 15
            
            # Check collision with Guard Hitbox
            if (gx < self.x + 16 and gx + gw > self.x and
                gy < self.y + 16 and gy + gh > self.y):
                
                if player.facingLeft:
                    self.knockback_vx = -5 
                else:
                    self.knockback_vx = 5

    def Damage(self, bullets):
        if self.hp <= 0:
            return
            
        for b in bullets:
            if (self.x < b.x + 2 and self.x + 16 > b.x and self.y < b.y + 2 and self.y + 16 > b.y):
                self.hp -= 1
                b.life = 0
