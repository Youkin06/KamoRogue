import pyxel

class Enemy1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 2
        self.size = 4
        self.color = 8 # red
        self.hp = 10    

    def update(self):
        if self.hp > 0:
            self.x += self.vx
            
            # Turn around at screen edges
            if self.x < 0:
                self.x = 0
                self.vx *= -1
            if self.x > 160 - 16: # 16 is approx sprite width
                self.x = 160 - 16
                self.vx *= -1
    
    def Damage(self, bullets):
        if self.hp <= 0:
            return
            
        for b in bullets:
            # Bullet size 2x2, Enemy size 16x16
            if (self.x < b.x + 2 and
                self.x + 16 > b.x and
                self.y < b.y + 2 and
                self.y + 16 > b.y):
                self.hp -= 1
                b.life = 0 # Destroy bullet

    def draw(self):
        if self.hp > 0:
            # Draw a red square for now
            pyxel.rect(self.x, self.y, 16, 16, self.color)
            # Or if we want to use sprite:
            # pyxel.blt(self.x, self.y, 0, 48, 0, 16, 16, 0) # Assuming some sprite at 48
