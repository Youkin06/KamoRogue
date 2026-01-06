import pyxel
import PyxelUniversalFont as puf

class AbilitySelectScene:
    def __init__(self):
        self.writer = puf.Writer("misaki_gothic.ttf")

        self.selected_index = 0
        self.options = []
        self.player = None

    def set_options(self, options, player):
        self.options = options
        self.player = player
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
                
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.options and self.player:
                selected_ability = self.options[self.selected_index]
                print(selected_ability.name)
                selected_ability.apply(self.player.playerAbility)
                # Ensure we don't apply multiple times in loop, maybe switch state back or something?
                # User didn't specify next step, just print and apply. 
                # I'll leave state as is for now as requested.

    def draw(self):
        self.writer.draw(45, 20, "ABILITY SELECT", 10, 16)
        
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

            # Draw Ability Icon (if options exist)
            if i < len(self.options):
                ability = self.options[i]
                pyxel.blt(x + 8, y + 8, 0, ability.u, ability.v, 16, 16, 0)
                
                # Draw Ability Name (y=66)
                name = ability.name
                name_x = x + 16 - (len(name) * 4) // 2
                pyxel.text(name_x, 66, name, 7)
                
                # Draw Ability Description (y=74)
                desc = ability.description
                desc_x = x + 16 - (len(desc) * 4) // 2
                pyxel.text(desc_x, 74, desc, 7)

        # Draw Controls
        # Left Control (Closer to center)
        # Arrow Left (32, 96) -> x=40
        pyxel.blt(40, 100, 0, 32, 96, 16, 16, 0)
        # Key A (0, 96) -> x=56
        pyxel.blt(56, 100, 0, 0, 96, 16, 16, 0)
        
        # Right Control (Closer to center)
        # Key D (16, 96) -> x=88
        pyxel.blt(88, 100, 0, 16, 96, 16, 16, 0)
        # Arrow Right (32, 96) flipped -> x=104
        pyxel.blt(104, 100, 0, 32, 96, -16, 16, 0)
        