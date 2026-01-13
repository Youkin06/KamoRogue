import pyxel

class EnemyBullet:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = 60 # Time to live in frames (optional cleanup)
        self.is_active = True
        self.animation_frame = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        self.animation_frame += 1
        
        # Screen bounds check (optional, but good practice)
        if self.x < -8 or self.x > 320 or self.life <= 0:
            self.is_active = False

    def draw(self):
        if not self.is_active:
            return
            
        # Animation: (0,144) -> (8,144) -> (16,144)
        # Cycle every few frames? User didn't specify speed. Standard 4-6 frames?
        cycle = (self.animation_frame // 4) % 3
        u = cycle * 8
        v = 144
        
        w = 8
        if self.vx < 0:
            w = -8
        
        pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, v, w, 8, 0, scale=2.0)
