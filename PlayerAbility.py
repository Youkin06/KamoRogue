import pyxel

class Ability:
    def __init__(self, name, apply_func):
        self.name = name
        self.apply = apply_func

def apply_double_jump(player_ability):
    player_ability.jumpMaxCount = 2

def apply_dash(player_ability):
    player_ability.CanDash = True

def apply_shield(player_ability):
    player_ability.CanGuard = True

ability_list = [
    Ability("Double Jump", apply_double_jump),
    Ability("Dash", apply_dash),
    Ability("Shield", apply_shield)
]

class PlayerAbility:
    def __init__(self):
        self.jumpMaxCount = 1
        self.CanDash = False
        self.CanGuard = False
        


