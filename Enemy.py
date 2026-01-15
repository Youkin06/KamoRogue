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
        self.hit_timer = 0
        
        # Hitbox parameters (Default)
        self.hitbox_offset_x = 2
        self.hitbox_offset_y = 1
        self.hitbox_width = 12
        self.hitbox_height = 14

    def update(self, player):
        # Knockback Physics
        self.x += self.knockback_vx
        self.knockback_vx *= 0.9
        if abs(self.knockback_vx) < 0.1:
            self.knockback_vx = 0

        if self.hit_timer > 0:
            self.hit_timer -= 1

        self.update_effects()

        # Guard Collision
        if player.guarding and player.guardHeight > 0.1 and self.knockback_vx == 0:
            gx = player.x
            gy = player.y
            gw = 8
            gh = 16
            
            if player.facingLeft:
                gx = player.x - 7
            else:
                gx = player.x + 15
            
            # Check collision with Guard Hitbox
            if (gx < self.x + 14 and gx + gw > self.x + 2 and
                gy < self.y + 15 and gy + gh > self.y + 1):
                
                if player.facingLeft:
                    self.knockback_vx = -5 
                else:
                    self.knockback_vx = 5

    def Damage(self, bullets):
        if self.hp <= 0:
            return
            
        for b in bullets:
            # Bullet 8x8 vs Enemy 12x14 (Offset 2, 1)
            if (self.x + 2 < b.x + 8 and self.x + 14 > b.x and 
                self.y + 1 < b.y + 8 and self.y + 15 > b.y):
                self.hp -= b.damage
                self.hit_timer = 2
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
