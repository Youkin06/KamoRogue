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
    player_ability.acquired_abilities.append("double_jump")

def apply_dash(player_ability):
    player_ability.CanDash = True
    player_ability.acquired_abilities.append("dash")

def apply_shield(player_ability):
    player_ability.CanGuard = True
    player_ability.acquired_abilities.append("shield")

ability_list = [
    Ability("ダブルジャンプ", 32, 112, "Wキーを二回押す", apply_double_jump),
    Ability("ダッシュ", 48, 112, "方向キー（ADキー）を二度押す", apply_dash),
    Ability("シールド", 16, 112, "Kキーを押す", apply_shield)
]

class PlayerAbility:
    def __init__(self):
        self.jumpMaxCount = 1
        self.CanDash = False
        self.CanGuard = True
        self.acquired_abilities = []
        


