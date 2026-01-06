import pyxel
import Player
import StageTest

class GameManager:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.load("my_resource.pyxres")
        
        self.player = Player.Player()
        self.stage = StageTest.StageTest()
        self.player = Player.Player()
        self.stage = StageTest.StageTest()
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
                
        elif self.currentSceneState == 2:
            pass 
        elif self.currentSceneState == 3:
            pass

    def draw(self):
        pyxel.cls(0)
        
        if self.currentSceneState == 0:
            pyxel.text(50, 50, "KAMO ROGUE", 7)
            pyxel.text(45, 70, "PRESS ENTER TO START", 7)
            
        elif self.currentSceneState == 1:
            self.stage.draw()
            self.player.draw()
            
        elif self.currentSceneState == 2:
            pyxel.text(60, 50, "GAME OVER", 7)
        elif self.currentSceneState == 3:
            pyxel.text(50, 50, "AbilitySelect", 7)
