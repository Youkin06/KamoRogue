import pyxel

class Stage:
    def __init__(self):
        self.enemies = []
        self.collision_tiles = []

    def update(self, player):
        new_enemies = []
        for enemy in self.enemies:
            enemy.update(player)
            enemy.Damage(player.bullets)
            if enemy.hp > 0 or (hasattr(enemy, "deathEffectTime") and enemy.deathEffectTime < 30):
                new_enemies.append(enemy)
        self.enemies = new_enemies
            
    def draw(self):
        for enemy in self.enemies:
            enemy.draw()