import pyxel

class EnemyBullet:
    def __init__(self, x, y, vx, vy, img_v=144):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.img_v = img_v
        self.life = 60 # 生存期間（フレーム数）
        self.is_active = True
        self.animation_frame = 0

    def update(self, *args):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        self.animation_frame += 1
        
        # 画面外チェック (オプションだが、良い習慣)
        if self.x < -8 or self.x > 320 or self.life <= 0:
            self.is_active = False

    def draw(self):
        if not self.is_active:
            return
            
        # アニメーション: (0,144) -> (8,144) -> (16,144)
        # 数フレームごとにサイクル？ユーザー指定なし。標準4-6フレーム？
        cycle = (self.animation_frame // 4) % 3
        u = cycle * 8
        v = self.img_v
        
        w = 8
        if self.vx < 0:
            w = -8
        
        pyxel.blt(self.x * 2 + 8, self.y * 2 + 8, 0, u, v, w, 8, 0, scale=2.0)
