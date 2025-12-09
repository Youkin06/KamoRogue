import pyxel

class Bullet:
    def __init__(self, x, y, facingLeft):
        self.x = x 
        self.y = y + 5
        self.facingLeft = facingLeft
        if facingLeft:
            self.x += -2 #初期ショット位置調整
            self.vx = -4
        else:
            self.x += 16 #初期ショット位置調整
            self.vx = 4
        self.life = 20

    def update(self):
        self.x += self.vx
        self.life -= 1
        return self.life > 0


    def draw(self):
        pyxel.rect(self.x, self.y, 2, 2, 10)