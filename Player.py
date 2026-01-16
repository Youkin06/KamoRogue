import pyxel
import Bullet
import Zanzou
import PlayerUI
import PlayerAbility


class Player:
    def __init__(self):
        #HP
        self.hp = 3
        self.max_hp = 3
        self.MutekiTime = 0
        self.UI = PlayerUI.PlayerUI(self)
        self.playerAbility = PlayerAbility.PlayerAbility()
        
        #移動move
        self.x = 80
        self.y = 0
        self.vx = 0 #x軸方向の速度
        self.vy = 0 #y軸方向の速度
        self.speed = 1.5
        self.size = 4
        self.color = 8

        #ジャンプjump
        self.gravity = 1
        # self.jumpMaxCount = 2
        self.jumpCount = 0
        self.jump_strength = -9
        self.is_grounded = False
        
        # ダッシュdash
        self.last_key = None
        self.key_timer = 0
        self.dash_distance = 20
        self.facingLeft = False
        
        #攻撃attack
        self.attack_power = 1
        self.bullets = []
        self.Bullet = Bullet.Bullet
        
        #残像Zanzou 
        self.zanzou = []
        self.Zanzou = Zanzou.Zanzou

        #画像image
        pyxel.load("my_resource.pyxres")
        
        #ガードguard
        self.guarding = False
        self.guardMaxHeight = 16.0
        self.guardHeight = 16.0
        
        # Floor
        self.stage_index = 1
        
    def update(self, stage=None):
        self.move(stage)
        self.attack()
        self.guard()
        if stage:
            self.reflect_bullets(stage.enemies)
        self.update_zanzou()
        self.UI.update()
        
        if self.MutekiTime > 0:
            self.MutekiTime -= 1
        

    def move(self, stage=None):
        self.key_timer += 1
        
        # Dash Left
        if pyxel.btnp(pyxel.KEY_A):
            if self.last_key == pyxel.KEY_A and self.key_timer < 10 and self.playerAbility.CanDash == True:
                self.zanzou.append(self.Zanzou(self.x, self.y, 32, 0, True, 5))
                self.zanzou.append(self.Zanzou(self.x - self.dash_distance // 2.5, self.y, 48, 0, True, 10))
                self.x -= self.dash_distance
            
            self.last_key = pyxel.KEY_A
            self.key_timer = 0
            
        # Dash Right    
        if pyxel.btnp(pyxel.KEY_D):
            if self.last_key == pyxel.KEY_D and self.key_timer < 10 and self.playerAbility.CanDash == True:
                self.zanzou.append(self.Zanzou(self.x, self.y, 32, 0, False, 5))
                self.zanzou.append(self.Zanzou(self.x + self.dash_distance // 1.5, self.y, 48, 0, False, 10))
                self.x += self.dash_distance

            self.last_key = pyxel.KEY_D
            self.key_timer = 0
            
        # Horizontal Movement
        vx = 0
        if pyxel.btn(pyxel.KEY_A):
            vx = -self.speed
            self.facingLeft = True
            
        if pyxel.btn(pyxel.KEY_D):
            vx = self.speed
            self.facingLeft = False
        
        self.x += vx
        
        # Horizontal Collision with Stage
        if stage:
            for tile in stage.collision_tiles:
                tx, ty = tile[0] * 8, tile[1] * 8
                if (self.x < tx + 8 and self.x + 16 > tx and
                    self.y < ty + 8 and self.y + 16 > ty):
                    # Collision detected
                    if vx > 0: # Moving Right
                        self.x = tx - 16
                    elif vx < 0: # Moving Left
                        self.x = tx + 8
            
        # Screen bounds
        if stage:
            if self.x < stage.limit_x_min:
                self.x = stage.limit_x_min
            if self.x > stage.limit_x_max:
                self.x = stage.limit_x_max
        else:
            if self.x < 0:
                self.x = 0
            if self.x > 160 - 16:
                self.x = 160 - 16
            
        if pyxel.btnp(pyxel.KEY_W) and self.is_grounded and self.jumpCount < self.playerAbility.jumpMaxCount:
            self.vy = self.jump_strength
            #self.is_grounded = False
            self.jumpCount += 1
            
        self.vy += self.gravity
        self.y += self.vy
        
        # Vertical Collision with Stage
        if stage:
            for tile in stage.collision_tiles:
                tx, ty = tile[0] * 8, tile[1] * 8
                if (self.x < tx + 8 and self.x + 16 > tx and
                    self.y < ty + 8 and self.y + 16 > ty):
                    # Collision detected
                    if self.vy > 0: # Falling
                        self.y = ty - 16
                        self.vy = 0
                        self.is_grounded = True
                        self.jumpCount = 0
                    elif self.vy < 0: # Jumping up
                        self.y = ty + 8
                        self.vy = 0
        
        # Simple floor collision
        if self.y > 88:
            self.y = 88
            self.vy = 0
            self.is_grounded = True
            self.jumpCount = 0

    def attack(self):
        new_bullets = []
        for i in self.bullets:
            if i.update():
                new_bullets.append(i)
        self.bullets = new_bullets

        if pyxel.btnp(pyxel.KEY_J):
            self.bullets.append(self.Bullet(self.x, self.y, self.facingLeft, self.attack_power))

    def guard(self):
        if pyxel.btn(pyxel.KEY_K) and self.playerAbility.CanGuard == True:
            self.guarding = True
            self.guardHeight -= 0.07
            if self.guardHeight < 0:
                self.guardHeight = 0
        else:
            self.guarding = False
            self.guardHeight += 0.5
            if self.guardHeight > self.guardMaxHeight:
                self.guardHeight = self.guardMaxHeight

    def update_zanzou(self):
        new_zanzou = []
        for g in self.zanzou:
            if g.update():
                new_zanzou.append(g)
        self.zanzou = new_zanzou

    def draw(self):
        self.zanzouDraw()
        self.bulletDraw()
        self.guardDraw()
        self.playerDraw() #一番下にすることで、一番手前に表示
        self.UI.draw()
        
    def Damage(self, enemies):
        if self.MutekiTime > 0:
            return

        for enemy in enemies:
            # Check collision with enemy bullets
            if hasattr(enemy, "bullets"):
                for b in enemy.bullets:
                    # Bullet 8x8 vs Player 16x16
                    # Use slightly smaller hitboxes for better feel
                    if (b.is_active and 
                        self.x < b.x + 6 and self.x + 16 > b.x + 2 and
                        self.y < b.y + 6 and self.y + 16 > b.y + 2):
                        
                        self.hp -= 1
                        self.MutekiTime = 60
                        b.is_active = False
                        return

            if enemy.hp <= 0:
                continue

            # Custom Hitbox Collision
            ex = enemy.x + getattr(enemy, 'hitbox_offset_x', 2)
            ey = enemy.y + getattr(enemy, 'hitbox_offset_y', 1)
            ew = getattr(enemy, 'hitbox_width', 12)
            eh = getattr(enemy, 'hitbox_height', 14)

            if (self.x + 4 < ex + ew and self.x + 12 > ex and 
                self.y + 2 < ey + eh and self.y + 16 > ey):
                self.hp -= 1
                self.MutekiTime = 60
                return
        

    def bulletDraw(self):
        for i in self.bullets:
            i.draw()

    def zanzouDraw(self):
        for g in self.zanzou:
            g.draw()

    def guardDraw(self):
        if self.guarding and self.guardHeight > 0:
            num_frames = 5
            frame_index = 4 - int(self.guardHeight / (self.guardMaxHeight / num_frames))
            
            if frame_index < 0: 
                frame_index = 0
            if frame_index > 4: 
                frame_index = 4

            u = frame_index * 8
            v = 16
            w = 8
            h = 16
            sy = self.y
            
            if self.facingLeft:
                sx = self.x - 7
                w = -8 
            else:
                sx = self.x + 15

            pyxel.blt(sx * 2 + 4, sy * 2 + 8, 0, u, v, w, h, 0, scale=2.0)

    def playerDraw(self):
        if self.MutekiTime > 0 and self.MutekiTime % 6 < 5:
            return

        u = (pyxel.frame_count // 6 % 2) * 16
        w = 16
        if self.facingLeft:
            w = -16
        pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, 0, w, 16, 0, scale=2.0)

    
    def reflect_bullets(self, enemies):
        if not self.guarding or self.guardHeight < 0.1:
            return

        # Shield Hitbox
        gw = 8
        gh = 16
        gy = self.y
        if self.facingLeft:
            gx = self.x - 7
        else:
            gx = self.x + 15

        for enemy in enemies:
            if hasattr(enemy, "bullets"):
                for b in enemy.bullets:
                    if not b.is_active:
                        continue
                        
                    # Bullet 8x8 vs Shield 8x16
                    # Check collision
                    if (gx < b.x + 8 and gx + gw > b.x and
                        gy < b.y + 8 and gy + gh > b.y):
                        
                        # Reflect only if moving towards the player/shield
                        if self.facingLeft and b.vx > 0:
                             b.vx *= -1
                             b.x += b.vx # Move it a bit to avoid immediate re-collision?
                        elif not self.facingLeft and b.vx < 0:
                             b.vx *= -1
                             b.x += b.vx
