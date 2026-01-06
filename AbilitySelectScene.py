import pyxel

class AbilitySelectScene:
    def __init__(self):
        self.selected_index = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_A):
            self.selected_index -= 1
            if self.selected_index < 0:
                self.selected_index = 0
                
        if pyxel.btnp(pyxel.KEY_D):
            self.selected_index += 1
            if self.selected_index > 2:
                self.selected_index = 2

    def draw(self):
        pyxel.text(50, 20, "AbilitySelect", 7)
        
        # Define box positions
        box_positions = [(16, 30), (64, 30), (112, 30)]
        
        # Draw boxes
        for i, pos in enumerate(box_positions):
            x, y = pos
            pyxel.blt(x, y, 0, 0, 64, 32, 32, 0)
            
            # Draw highlight if selected
            if i == self.selected_index:
                # pyxel.rectb(x-1, y-1, 34, 34, 10) 
                # Draw sprite highlight (32, 64) size 32x32
                pyxel.blt(x, y, 0, 32, 64, 32, 32, 0)

        # Draw Controls
        # Left Control (Under Left Box)
        # Arrow Left (32, 96) -> x=16
        pyxel.blt(16, 70, 0, 32, 96, 16, 16, 0)
        # Key A (0, 96) -> x=32
        pyxel.blt(32, 70, 0, 0, 96, 16, 16, 0)
        
        # Right Control (Under Right Box)
        # Key D (16, 96) -> x=112
        pyxel.blt(112 + 10 , 70, 0, 16, 96, 16, 16, 0)
        # Arrow Right (32, 96) flipped -> x=128
        pyxel.blt(128 - 10, 70, 0, 32, 96, -16, 16, 0)
        