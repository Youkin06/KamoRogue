import PyxelUniversalFont
import pyxel

class Ability:
    def __init__(self, id, name, u, v, description, apply_func, repeatable=False):
        self.id = id
        self.name = name
        self.u = u
        self.v = v
        self.description = description
        self.apply = apply_func
        self.repeatable = repeatable

def apply_double_jump(player):
    player.playerAbility.jumpMaxCount = 2
    player.playerAbility.acquired_abilities.append("double_jump")

def apply_dash(player):
    player.playerAbility.CanDash = True
    player.playerAbility.acquired_abilities.append("dash")

def apply_shield(player):
    player.playerAbility.CanGuard = True
    player.playerAbility.acquired_abilities.append("shield")

def apply_heart(player):
    player.max_hp += 1
    player.hp = player.max_hp
    player.playerAbility.acquired_abilities.append("heart")

ability_list = [
    Ability("double_jump", "ダブルジャンプ", 32, 112, "Wキーを二回押す", apply_double_jump),
    Ability("dash", "ダッシュ", 48, 112, "方向キー（ADキー）を二度押す", apply_dash),
    Ability("shield", "シールド", 16, 112, "Kキーを押す", apply_shield),
    Ability("heart", "ハート", 64, 112, "最大HP+1 & 全回復", apply_heart, repeatable=True)
]

class PlayerAbility:
    def __init__(self):
        self.jumpMaxCount = 1
        self.CanDash = False
        self.CanGuard = False
        self.acquired_abilities = []
        


