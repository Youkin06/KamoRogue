import pyxel

class PlayerUI:
    def __init__(self, player):
        self.player = player
    
    def update(self):
        pass

    def draw(self):
        self.HPdraw()
        self.AbilityDraw()
        self.FloorDraw()
        
    def HPdraw(self):
        for i in range(self.player.hp):
            # 6 hearts per row
            row = i // 6
            col = i % 6
            
            x = (5 + col * 10) * 2 + 4
            draw_y = 5 * 2 + 4 + row * 20 # Add vertical spacing
            
            pyxel.blt(x, draw_y, 0, 0, 32, 8, 8, 0, scale=2.0)

    def AbilityDraw(self):
        start_x = 300
        y = 14
        spacing = 20
        
        ability_coords = {
            "shield": (16, 32),
            "double_jump": (24, 32),
            "dash": (32, 32),
            "heart": (40, 32)
        }
        
        for i, ability_name in enumerate(self.player.playerAbility.acquired_abilities):
            if ability_name in ability_coords:
                u, v = ability_coords[ability_name]
                
                # Multi-row logic: 7 items per row
                row = i // 7
                col = i % 7
                
                x = start_x - col * spacing
                draw_y = y + row * 20 # Add vertical spacing for new rows
                
                pyxel.blt(x, draw_y, 0, u, v, 8, 8, 0, scale=2.0)

    def FloorDraw(self):
        # Center of screen (320 width -> 160 center)
        # Image width 16 (scaled by 2 -> 32)
        # x = 160 - 32/2 = 144
        x = 144
        y = 14 # Same as HP
        
        # Calculate u based on stage_index
        # Stage 1: 64, Stage 2: 80 ...
        u = 64 + (self.player.stage_index - 1) * 16
        v = 0
        w = 16
        h = 8
        
        pyxel.blt(x, y, 0, u, v, w, h, 0, scale=2.0)
