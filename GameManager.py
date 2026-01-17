import pyxel
import Player
import Stage1
import Stage2
import Stage3
import Stage4
import Stage4
import Stage5
import HowToPlayScene
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
        self.howToPlayScene = HowToPlayScene.HowToPlayScene()
        self.abilitySelectScene = AbilitySelectScene.AbilitySelectScene()
        self.howToPlayScene = HowToPlayScene.HowToPlayScene()
        self.currentSceneState = 0 # 0: Title, 1: Game, 2: Result, 3: AbilitySelect, 4: HowToPlay
        
        self.title_y = -64 # Start off-screen
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.currentSceneState == 0:
            if self.title_y < 88:
                self.title_y += 4 # Animation speed
            
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.title_y = 88 # Ensure finished if skipped? Or just proceed
                self.currentSceneState = 4 # Go to HowToPlay
                
        elif self.currentSceneState == 4:
            if self.howToPlayScene.update():
                self.currentSceneState = 1 # Go to Game
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y
                
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
                self.title_y = -64 # Reset animation
                self.player = Player.Player()
                self.currentSceneState = 0
                self.player = Player.Player()
                self.stage = Stage1.Stage1()
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y 
        elif self.currentSceneState == 3:
            if self.abilitySelectScene.update():
                if self.player.stage_index == 1:
                    self.stage = Stage2.Stage2()
                    self.player.stage_index = 2
                elif self.player.stage_index == 2:
                    self.stage = Stage3.Stage3()
                    self.player.stage_index = 3
                elif self.player.stage_index == 3:
                     self.stage = Stage4.Stage4()
                     self.player.stage_index = 4
                elif self.player.stage_index == 4:
                     self.stage = Stage5.Stage5()
                     self.player.stage_index = 5
                
                self.currentSceneState = 1
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y
                
                self.player.vy = 0

        
    def TitleDraw(self):
         # Draw Background (Tilemap 0, Start x=0, y=16)
        base_ty = 16
        for ty in range(15):
            for tx in range(20):
                tile = pyxel.tilemaps[0].pget(tx, base_ty + ty)
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16, ty * 16, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        # Title Image
        # x = 114 (79+35), y = self.title_y
        pyxel.blt(114, self.title_y, 0, 0, 184, 81, 32, 0, scale=2.0)
        
        # Only show text if animation finished (optional, but looks cleaner) or just always
        if self.title_y >= 88:
            #pyxel.text(90, 160, "PRESS ENTER TO START", 7)
            #Enterキー
            pyxel.blt(100+30+10 -20, 200-8 -20, 0, 48, 96, 25, 13, 0, scale=2.0)
            #CONFILM文字
            pyxel.text(160, 185, "TO START",7)

    def draw(self):
        pyxel.cls(0)
        
        if self.currentSceneState == 0:
            self.TitleDraw()
            
        elif self.currentSceneState == 1:
            self.stage.draw()
            self.player.draw()
            
        elif self.currentSceneState == 2:
            pyxel.text(140, 100, "GAME OVER", 7)
            pyxel.text(130, 120, "PRESS R TO RESTART", 7)
        elif self.currentSceneState == 3:
            self.abilitySelectScene.draw()
        elif self.currentSceneState == 4:
            self.howToPlayScene.draw()
