import pyxel

class BulletEffect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frameTimer = 0
        self.frameIndex = 0
        self.life = True

    def update(self):
        self.frameTimer += 1
        if self.frameTimer % 2 == 0: 
            self.frameIndex += 1
        
        if self.frameIndex >= 3:
            self.life = False
            return False
        return True

    def draw(self):
        u = 24 + self.frameIndex * 8
        pyxel.blt(self.x * 2 + 4, self.y * 2 + 4, 0, u, 40, 8, 8, 0, scale=2.0)
