
import pyxel

class App:
    def __init__(self):
        # 32x32 window
        pyxel.init(32, 32)
        # Create a single white pixel image
        pyxel.images[0].set(0, 0, ["1"])
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        # Draw 1x1 pixel at 10,10. Scaled 10x.
        # w=1, h=1. Center 10.5, 10.5?
        # If Pyxel uses center (x+w/2), for w=1, is it integer division? 10+0 = 10?
        # Or float?
        # Let's try w=2, h=2. At 10,10.
        # Center 11,11.
        # Scale 2.0. Result 4x4.
        # Should be centered at 11,11.
        # TopLeft: 11 - 2 = 9.
        # Original TopLeft: 10.
        # Shift: -1. (w/2 * (scale-1)) = 1 * 1 = 1.
        
        # Test 1: Draw w=8, h=8 at 0,0. Scale 1 (White)
        pyxel.rectb(0, 0, 8, 8, 7)
        
        # Test 2: Draw w=8, h=8 at 0,16. Scale 2 (Red)
        # Expected: Shifted by -4? So starts at -4, 12?
        pyxel.blt(0, 16, 0, 0, 0, 8, 8, 8, scale=2.0)
        
        # Mark logical Top-Left (0, 16) with Green dot
        pyxel.pset(0, 16, 11)

App()
