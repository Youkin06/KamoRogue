import pyxel

class PlayerUI:
    def __init__(self, player):
        self.player = player

    def update(self):
        pass

    def draw(self):
        # 左上にHPを表示
        # Display HP at top-left
        pyxel.text(5, 5, f"HP: {self.player.hp}", 7)
