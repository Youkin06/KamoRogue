import pyxel
import BulletEffect

class Enemy:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.vx = 0
        self.knockback_vx = 0
        self.color = 8
        self.effects = []

    def update(self, player):
        # Knockback Physics
        self.x += self.knockback_vx
        self.knockback_vx *= 0.9
        if abs(self.knockback_vx) < 0.1:
            self.knockback_vx = 0

        self.update_effects()

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
            if (self.x + 4 < b.x + 2 and self.x + 12 > b.x and self.y < b.y + 2 and self.y + 16 > b.y):
                self.hp -= 1
                b.life = 0
                
                FinalX = b.x
                FinalY = b.y
                self.effects.append(BulletEffect.BulletEffect(FinalX, FinalY))

    def draw_effects(self):
        for effect in self.effects:
            effect.draw()

    def update_effects(self):
        new_effects = []
        for effect in self.effects:
            if effect.update():
                new_effects.append(effect)
        self.effects = new_effects
