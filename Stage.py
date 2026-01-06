import pyxel

class Stage:
    def __init__(self):
        self.enemies = []
        self.collision_tiles = []

    def update(self, player):
        for enemy in self.enemies:
            enemy.update(player)
            enemy.Damage(player.bullets)
            
    def draw(self):
        for enemy in self.enemies:
            enemy.draw()