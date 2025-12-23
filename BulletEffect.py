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
        pyxel.blt(self.x, self.y, 0, u, 40, 8, 8, 0)
