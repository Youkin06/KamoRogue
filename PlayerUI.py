import pyxel

class PlayerUI:
    def __init__(self, player):
        self.player = player
    
    def update(self):
        pass

    def draw(self):
        self.HPdraw()
        self.AbilityDraw()
        
    def HPdraw(self):
        for i in range(self.player.hp):
            pyxel.blt((5 + i * 10) * 2 + 4, 5 * 2 + 4, 0, 0, 32, 8, 8, 0, scale=2.0)

    def AbilityDraw(self):
        # Draw acquired abilities from right to left
        # Start X = 320 - 20 (padding)
        # Y = 14 (same as HP)
        start_x = 300
        y = 14
        spacing = 20
        
        # Coordinates mapping
        ability_coords = {
            "shield": (16, 32),
            "double_jump": (24, 32),
            "dash": (32, 32)
        }
        
        for i, ability_name in enumerate(self.player.playerAbility.acquired_abilities):
            if ability_name in ability_coords:
                u, v = ability_coords[ability_name]
                x = start_x - i * spacing
                pyxel.blt(x, y, 0, u, v, 8, 8, 0, scale=2.0)
