import pyxel
import Player
import Stage1
import Stage2
import AbilitySelectScene
import random
import PlayerAbility

class GameManager:
    def __init__(self):
        pyxel.init(320, 240, fps=30)
        pyxel.load("my_resource.pyxres")
        
        self.player = Player.Player()
        self.stage = Stage1.Stage1()

        self.abilitySelectScene = AbilitySelectScene.AbilitySelectScene()
        self.currentSceneState = 0 # 0: Title, 1: Game, 2: Result, 3: AbilitySelect
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.currentSceneState == 0:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.currentSceneState = 1
                
        elif self.currentSceneState == 1:
            self.player.update(self.stage)
            self.stage.update(self.player)
            self.player.Damage(self.stage.enemies)
            
            if self.player.hp <= 0:
                self.currentSceneState = 2
                
            if len(self.stage.enemies) == 0:
                self.currentSceneState = 3
                selected_abilities = random.sample(PlayerAbility.ability_list, 3)
                self.abilitySelectScene.set_options(selected_abilities, self.player)
                
        elif self.currentSceneState == 2:
            pass 
        elif self.currentSceneState == 3:
            if self.abilitySelectScene.update():
                self.stage = Stage2.Stage2()
                self.currentSceneState = 1
                self.player.x = 80
                self.player.y = 0
                self.player.vy = 0
                self.player.stage_index = 2

    def draw(self):
        pyxel.cls(0)
        
        if self.currentSceneState == 0:
            pyxel.text(100, 100, "KAMO ROGUE", 7)
            pyxel.text(90, 140, "PRESS ENTER TO START", 7)
            
        elif self.currentSceneState == 1:
            self.stage.draw()
            self.player.draw()
            
        elif self.currentSceneState == 2:
            pyxel.text(120, 100, "GAME OVER", 7)
        elif self.currentSceneState == 3:
            self.abilitySelectScene.draw()
