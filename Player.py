import pyxel
import Bullet


class Player:
    def __init__(self):
        #移動move
        self.x = 80
        self.y = 0
        self.vx = 0 #x軸方向の速度
        self.vy = 0 #y軸方向の速度
        self.speed = 1
        self.size = 4
        self.color = 8
        self.gravity = 1
        self.jump_strength = -8
        self.is_grounded = False
        
        # ダッシュdash
        self.last_key = None
        self.key_timer = 0
        self.dash_distance = 15
        self.facingLeft = False
        self.bullets = []

        #攻撃attack
        self.Bullet = Bullet.Bullet

        #画像image
        pyxel.load("my_resource.pyxres")
        
    def update(self):
        self.move()
        self.attack()
        

    def move(self):
        self.key_timer += 1
        
        # Dash Left
        if pyxel.btnp(pyxel.KEY_A):
            if self.last_key == pyxel.KEY_A and self.key_timer < 10:
                self.x -= self.dash_distance
            
            self.last_key = pyxel.KEY_A
            self.key_timer = 0
            
        # Dash Right
        if pyxel.btnp(pyxel.KEY_D):
            if self.last_key == pyxel.KEY_D and self.key_timer < 10:
                self.x += self.dash_distance

            self.last_key = pyxel.KEY_D
            self.key_timer = 0
            
        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.speed
            self.facingLeft = True
            
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.speed
            self.facingLeft = False
            
        if pyxel.btnp(pyxel.KEY_W) and self.is_grounded:
            self.vy = self.jump_strength
            self.is_grounded = False
            
        self.vy += self.gravity
        self.y += self.vy
        
        # Simple floor collision
        if self.y > 80:
            self.y = 80
            self.vy = 0
            self.is_grounded = True

    def attack(self):
        new_bullets = []
        for i in self.bullets:
            if i.update():
                new_bullets.append(i)
        self.bullets = new_bullets

        if pyxel.btnp(pyxel.KEY_J):
            self.bullets.append(self.Bullet(self.x, self.y, self.facingLeft))

    def draw(self):
        self.bulletDraw()
        self.playerDraw() #一番下にすることで、一番手前に表示
            

    def bulletDraw(self):
        for i in self.bullets:
            i.draw()

    def playerDraw(self):
        u = (pyxel.frame_count // 6 % 2) * 16
        w = 16
        if self.facingLeft:
            w = -16
        pyxel.blt(self.x, self.y, 0, u, 0, w, 16, 0)
