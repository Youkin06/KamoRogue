import pyxel

class Enemy1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 2
        self.size = 4
        self.color = 8 # red

    def update(self):
        self.x += self.vx
        
        # Turn around at screen edges
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.x > 160 - 16: # 16 is approx sprite width
            self.x = 160 - 16
            self.vx *= -1

    def draw(self):
        # Draw a red square for now
        pyxel.rect(self.x, self.y, 16, 16, self.color)
        # Or if we want to use sprite:
        # pyxel.blt(self.x, self.y, 0, 48, 0, 16, 16, 0) # Assuming some sprite at 48
