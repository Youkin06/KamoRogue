import pyxel

class PlayerUI:
    def __init__(self, player):
        self.player = player
    
    def update(self):
        pass

    def draw(self):
        self.HPdraw()
        
    def HPdraw(self):
        for i in range(self.player.hp):
            pyxel.blt(5 + i * 10, 5, 0, 0, 32, 8, 8, 0)
