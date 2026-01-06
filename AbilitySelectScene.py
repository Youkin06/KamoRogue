import pyxel

class AbilitySelectScene:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pyxel.text(50, 20, "AbilitySelect", 7)
        
        pyxel.blt(16, 30, 0, 0, 64, 32, 32, 0)
        pyxel.blt(64, 30, 0, 0, 64, 32, 32, 0)
        pyxel.blt(112, 30, 0, 0, 64, 32, 32, 0)
