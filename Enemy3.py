import pyxel
import Enemy
import EnemyBullet
import Toge
import random

class Enemy3(Enemy.Enemy):
    def __init__(self, x, y, min_x=0, max_x=144):
        super().__init__(x, y, 50) # HP 10
        self.vx = 0
        self.vy = 0
        self.gravity = 1
        self.min_x = min_x
        self.max_x = max_x
        self.size = 4
        self.color = 8
        self.deathEffectTime = 0
        self.bullets = []
        self.toge_timer = 0
        self.is_summoning = False
        self.summon_timer = 0
        self.shoot_timer = 0
        self.shoot_interval = 15
        self.facingLeft = True
        self.jump_timer = 0
        self.on_ground = False

    def update(self, player):
        if self.hp <= 0:
            self.deathEffectTime += 1
            self.update_effects()
            return 

        self.update_movement(player)
        self.update_shooting(player)
        self.update_bullets(player)
        self.TogeMake(player)
        super().update(player)

    def update_movement(self, player):
        # プレイヤーの方を向く
        if player.x < self.x:
            self.facingLeft = True
        else:
            self.facingLeft = False
            
        # 重力
        self.vy += self.gravity
        self.y += self.vy
        
        #ゆか
        if self.y > 88:
            self.y = 88
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False
            
        # ランダムジャンプ
        if self.on_ground and random.randint(0, 100) < 5: 
            self.vy = -7 # ジャンプパワー
            self.on_ground = False

    def update_shooting(self, player):
        if self.is_summoning:
            return
            
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_interval:
            self.shoot_timer = 0
            # プレイヤー方向向く
            b_vx = -2 if self.facingLeft else 2
            self.bullets.append(EnemyBullet.EnemyBullet(self.x, self.y, b_vx, 0, img_v=232))

    def TogeMake(self, player):
        if self.is_summoning:
            self.summon_timer -= 1
            if self.summon_timer <= 0:
                self.is_summoning = False
                # Toge生成
                spawn_x = player.x + random.randint(-10, 10)
                print("spawn_x: "+ str(spawn_x))
                self.bullets.append(Toge.Toge(spawn_x, 16, detection_range_tile=30))
        else:
            #とげ生成状態
            self.toge_timer += 1
            if self.toge_timer > 120:
                self.toge_timer = 0
                self.is_summoning = True
                self.is_summoning = True
                self.summon_timer = 60 
                

    def update_bullets(self, player):
        new_bullets = []
        for b in self.bullets:
            b.update(player)
            if b.is_active:
                new_bullets.append(b)
        self.bullets = new_bullets
    
    def TogeMakeDraw(self):
        u = 32
        if (pyxel.frame_count // 4) % 2 == 1:
            u = 48
        
        w = 16
        if self.facingLeft:
            w = -16
        else:
            w = 16
        
        pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 216, w, 16, 0, scale=2.0)

    def draw(self):
        if self.hp > 0:
            if self.is_summoning:
                self.TogeMakeDraw()
            else:
                u = (pyxel.frame_count // 6 % 2) * 16
                w = 16
                if self.facingLeft:
                    w = -16 
                else:
                    w = 16 
                
                if self.hit_timer > 0:
                    for i in range(1, 16):
                        pyxel.pal(i, 7)
                    
                # スプライト位置 (0, 216)
                pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 216, w, 16, 0, scale=2.0)
                
                if self.hit_timer > 0:
                    pyxel.pal()
        elif self.deathEffectTime < 30:
             u = (self.deathEffectTime // 10) * 16 + 32
             pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 216, 16, 16, 0, scale=2.0)
        
        for b in self.bullets:
            b.draw()

        self.draw_effects()
