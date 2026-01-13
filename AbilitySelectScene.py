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
                return True
        return False

    def draw(self):
        self.writer.draw(105, 40, "ABILITY SELECT", 16, 7)
        
        # Define box positions
        box_positions = [(16, 30), (64, 30), (112, 30)]
        
        # Draw boxes
        for i, pos in enumerate(box_positions):
            # Scale coordinates by 2
            x, y = pos
            draw_x = x * 2
            draw_y = y * 2
            
            # Draw box (32x32 -> scaled 2.0 -> 64x64) offset +16
            pyxel.blt(draw_x + 16, draw_y + 16, 0, 0, 64, 32, 32, 0, scale=2.0)
            
            # Draw highlight if selected
            if i == self.selected_index:
                # Draw sprite highlight (32, 64) size 32x32 -> scaled 2.0 offset +16
                pyxel.blt(draw_x + 16, draw_y + 16, 0, 32, 64, 32, 32, 0, scale=2.0)

            # Draw Ability Icon (if options exist)
            if i < len(self.options):
                ability = self.options[i]
                # Center icon in box (offset 8 originally -> 16 scaled)
                # Icon W=16 -> Offset +8
                # Pos: draw_x + 16. With Offset: draw_x + 16 + 8 = draw_x + 24
                pyxel.blt(draw_x + 24, draw_y + 24, 0, ability.u, ability.v, 16, 16, 0, scale=2.0)
                
                # Draw Ability Name (y=66 -> 132)
                name = ability.name
                # Centering for 8px font in 64px box:
                # TextWidth = len(name) * 8 (approx)
                # Start = draw_x + 32 - (len * 4)
                name_draw_x = draw_x + 32 - (len(name) * 4)
                self.writer.draw(name_draw_x, 132, name, 8, 7)
                
                # Draw Ability Description (y=74 -> 148)
                desc = ability.description
                desc_draw_x = draw_x + 32 - (len(desc) * 4)
                self.writer.draw(desc_draw_x, 148, desc, 8, 7)

        # Draw Controls (y=100 -> 200)
        # Left Control W=16 -> Offset +8
        pyxel.blt(80 + 8, 200 + 8, 0, 32, 96, 16, 16, 0, scale=2.0)
        pyxel.blt(112 + 8, 200 + 8, 0, 0, 96, 16, 16, 0, scale=2.0)
        
        # Right Control
        pyxel.blt(176 + 8, 200 + 8, 0, 16, 96, 16, 16, 0, scale=2.0)
        pyxel.blt(208 + 8, 200 + 8, 0, 32, 96, -16, 16, 0, scale=2.0)
        