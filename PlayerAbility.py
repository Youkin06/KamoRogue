import pyxel

class Ability:
    def __init__(self, name, u, v, apply_func):
        self.name = name
        self.u = u
        self.v = v
        self.apply = apply_func

def apply_double_jump(player_ability):
    player_ability.jumpMaxCount = 2

def apply_dash(player_ability):
    player_ability.CanDash = True

def apply_shield(player_ability):
    player_ability.CanGuard = True

ability_list = [
    Ability("Double Jump", 24, 32, apply_double_jump),
    Ability("Dash", 32, 32, apply_dash),
    Ability("Shield", 16, 32, apply_shield)
]

class PlayerAbility:
    def __init__(self):
        self.jumpMaxCount = 1
        self.CanDash = False
        self.CanGuard = False
        


