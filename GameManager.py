import pyxel
import Player
import Stage1
import Stage2
import Stage3
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
                # Filter available abilities
                available_abilities = []
                for ability in PlayerAbility.ability_list:
                    if ability.repeatable or ability.id not in self.player.playerAbility.acquired_abilities:
                        available_abilities.append(ability)
                
                # Sample up to 3 abilities
                sample_count = min(3, len(available_abilities))
                selected_abilities = random.sample(available_abilities, sample_count)
                
                self.abilitySelectScene.set_options(selected_abilities, self.player)
                
        elif self.currentSceneState == 2:
            if pyxel.btnp(pyxel.KEY_R):
                self.currentSceneState = 0
                self.player = Player.Player()
                self.stage = Stage1.Stage1() 
        elif self.currentSceneState == 3:
            if self.abilitySelectScene.update():
                if self.player.stage_index == 1:
                    self.stage = Stage2.Stage2()
                    self.player.stage_index = 2
                elif self.player.stage_index == 2:
                    self.stage = Stage3.Stage3()
                    self.player.stage_index = 3
                
                self.currentSceneState = 1
                self.player.x = 80
                self.player.y = 0
                self.player.vy = 0

    def draw(self):
        pyxel.cls(0)
        
        if self.currentSceneState == 0:
            pyxel.text(100, 100, "KAMO ROGUE", 7)
            pyxel.text(90, 140, "PRESS ENTER TO START", 7)
            
        elif self.currentSceneState == 1:
            self.stage.draw()
            self.player.draw()
            
        elif self.currentSceneState == 2:
            pyxel.text(140, 100, "GAME OVER", 7)
            pyxel.text(130, 120, "PRESS R TO RESTART", 7)
        elif self.currentSceneState == 3:
            self.abilitySelectScene.draw()
