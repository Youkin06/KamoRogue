import pyxel
import Enemy
import EnemyBullet

class Enemy2(Enemy.Enemy):
    def __init__(self, x, y, min_x=0, max_x=144):
        super().__init__(x, y, 1)#初期位置x,y,HP
        self.vx = 1
        self.min_x = min_x
        self.max_x = max_x
        self.size = 4
        self.color = 8
        self.deathEffectTime = 0
        self.bullets = []
        self.shoot_timer = 0
        self.shoot_interval = 60

    def update(self, player):
        if self.hp <= 0:
            self.deathEffectTime += 1
            self.update_effects()
            return 

        self.update_movement()
        self.update_shooting()
        self.update_bullets()
        super().update(player)

    def update_movement(self):
        self.x += self.vx
        if self.x < self.min_x:
            self.x = self.min_x
            self.vx *= -1
        if self.x > self.max_x:
            self.x = self.max_x
            self.vx *= -1

    def update_shooting(self):
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot_timer = 0
            # Fire in direction of movement
            # Bullet vx = self.vx * 2 (faster than enemy)
            b_vx = 2 if self.vx > 0 else -2
            self.bullets.append(EnemyBullet.EnemyBullet(self.x, self.y, b_vx, 0))

    def update_bullets(self):
        new_bullets = []
        for b in self.bullets:
            b.update()
            if b.is_active:
                new_bullets.append(b)
        self.bullets = new_bullets
    
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
             pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 128, 16, 16, 0, scale=2.0)
        
        for b in self.bullets:
            b.draw()

        self.draw_effects()
