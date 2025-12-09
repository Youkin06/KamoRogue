import pyxel

class Zanzou:
    def __init__(self, x, y, u, v, facingLeft, life):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.facingLeft = facingLeft
        self.life = life

    def update(self):
        self.life -= 1
        return self.life > 0

    def draw(self):
        # 32*0 の画像を使用
        _u = self.u
        _v = self.v
        w = 16
        if self.facingLeft:
            w = -16
        
        pyxel.blt(self.x, self.y, 0, _u, _v, w, 16, 0)
