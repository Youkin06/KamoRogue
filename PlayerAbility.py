import PyxelUniversalFont
import pyxel

class Ability:
    def __init__(self, name, u, v, description, apply_func):
        self.name = name
        self.u = u
        self.v = v
        self.description = description
        self.apply = apply_func

def apply_double_jump(player_ability):
    player_ability.jumpMaxCount = 2

def apply_dash(player_ability):
    player_ability.CanDash = True

def apply_shield(player_ability):
    player_ability.CanGuard = True

ability_list = [
    Ability("ダブルジャンプ", 32, 112, "Space", apply_double_jump),
    Ability("ダッシュ", 48, 112, "Move fast", apply_dash),
    Ability("シールド", 16, 112, "Block attacks", apply_shield)
]

class PlayerAbility:
    def __init__(self):
        self.jumpMaxCount = 1
        self.CanDash = False
        self.CanGuard = False
        


