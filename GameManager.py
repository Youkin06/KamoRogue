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

import PyxelUniversalFont as puf

class GameManager:
    def __init__(self):
        pyxel.init(320, 240, fps=30)
        pyxel.load("my_resource.pyxres")
        pyxel.playm(0, loop=True)
        
        self.player = Player.Player()
        self.stage = Stage1.Stage1()

        self.abilitySelectScene = AbilitySelectScene.AbilitySelectScene()
        self.howToPlayScene = HowToPlayScene.HowToPlayScene()
        self.abilitySelectScene = AbilitySelectScene.AbilitySelectScene()
        self.howToPlayScene = HowToPlayScene.HowToPlayScene()
        self.currentSceneState = 0 # 0: Title, 1: Game, 2: Result, 3: AbilitySelect, 4: HowToPlay
        
        self.title_y = -64 # 画面外から開始

        self.writer = puf.Writer("misaki_gothic.ttf")
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.currentSceneState == 0:
            if self.title_y < 88:
                self.title_y += 4 # アニメーション速度
            
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.title_y = 88 # スキップされた場合は完了状態にする
                self.currentSceneState = 4 # 遊び方画面へ
                
        elif self.currentSceneState == 4:
            if self.howToPlayScene.update():
                self.currentSceneState = 1 # ゲーム画面へ
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y
                
        elif self.currentSceneState == 1:
            self.player.update(self.stage)
            self.stage.update(self.player)
            self.player.Damage(self.stage.enemies)
            
            if self.player.hp <= 0:
                self.currentSceneState = 2
                
            #GameClear
            if len(self.stage.enemies) == 0:
                if self.player.stage_index == 5:
                    self.currentSceneState = 5 # Game Clear

                    pyxel.playm(0, loop=True) # 音楽を戻す等は任意
                else:
                    self.currentSceneState = 3
                    # 利用可能な能力をフィルタリング
                    available_abilities = []
                    for ability in PlayerAbility.ability_list:
                        if ability.repeatable or ability.id not in self.player.playerAbility.acquired_abilities:
                            available_abilities.append(ability)
                    
                    # 最大3つの能力をサンプリング
                    sample_count = min(3, len(available_abilities))
                    selected_abilities = random.sample(available_abilities, sample_count)
                    
                    self.abilitySelectScene.set_options(selected_abilities, self.player)
                
        elif self.currentSceneState == 2:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.currentSceneState = 0
                self.title_y = -64 # アニメーションをリセット
                self.player = Player.Player()
                self.stage = Stage1.Stage1()
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y 
                pyxel.playm(0, loop=True) 
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
                     pyxel.playm(2, loop=True)
                
                self.currentSceneState = 1
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y
                
                self.player.vy = 0
        elif self.currentSceneState == 5:
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.currentSceneState = 0
                self.title_y = -64
                self.player = Player.Player()
                self.stage = Stage1.Stage1()
                self.player.x = self.stage.player_start_x
                self.player.y = self.stage.player_start_y
                pyxel.playm(0, loop=True)

    def DrawBackground(self):
         # 背景を描画 (タイルマップ 0, 開始 x=0, y=16)
        base_ty = 16
        for ty in range(15):
            for tx in range(20):
                tile = pyxel.tilemaps[0].pget(tx, base_ty + ty)
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16, ty * 16, 1, src_x, src_y, 8, 8, 0, scale=2.0)

    def TitleDraw(self):
        self.DrawBackground()

        # Title Image
        # x = 114 (79+35), y = self.title_y
        pyxel.blt(114, self.title_y, 0, 0, 184, 81, 32, 0, scale=2.0)
        
        # アニメーション完了後にテキストを表示 (オプションだが、その方が綺麗) あるいは常に表示
        if self.title_y >= 88:
            #pyxel.text(90, 160, "PRESS ENTER TO START", 7)
            #Enterキー
            pyxel.blt(100+30+10 -20, 200-8 -20, 0, 48, 96, 25, 13, 0, scale=2.0)
            #CONFILM文字
            self.writer.draw(160, 185- 10   , "TO START", 16 ,7)

    def get_text_width(self, text, size):
        width = 0
        for char in text:
             # This is a rough estimation, mimicking what HowToPlayScene does or simpler since puf handles it
             # But for centering we might need puf's internal width or a heuristic
             if ord(char) < 256:
                 width += size / 2 # Simple assumption for ascii
             else:
                 width += size
        return width * len(text) # Very rough. puf doesn't expose measure easily here without looking at lib?
        # Actually puf usually handles drawing. Centering manually.
        # Let's just use fixed positions or simple heuristic.
        # "GAME OVER" is 9 chars. At size 24.
        pass

    def draw(self):
        pyxel.cls(0)
        
        if self.currentSceneState == 0:
            self.TitleDraw()
            
        elif self.currentSceneState == 1:
            self.stage.draw()
            self.player.draw()
            
        elif self.currentSceneState == 2:
            self.DrawBackground()
            #pyxel.text(140, 100, "GAME OVER", 7)
            self.writer.draw(110, 80, "GAME OVER", 24, 7) # Adjusted roughly to center
            
            # Enter key image
            pyxel.blt(160-60, 120, 0, 48, 96, 25, 13, 0, scale=2.0)
            #pyxel.text(220, 128, "TO RESTART", 7)
            self.writer.draw(220-60, 125, "TO RESTART", 16, 7)
        elif self.currentSceneState == 3:
            self.abilitySelectScene.draw()
        elif self.currentSceneState == 4:
            self.howToPlayScene.draw()
        elif self.currentSceneState == 5:
            self.DrawBackground()
            #pyxel.text(140, 100, "GAME CLEAR", 7)
            self.writer.draw(100, 80, "GAME CLEAR", 24, 7)
            
            # Enter key image
            pyxel.blt(160 -60, 120, 0, 48, 96, 25, 13, 0, scale=2.0)
            #pyxel.text(220, 128, "TO TITLE", 7)
            self.writer.draw(220 -60, 125, "TO TITLE", 16, 7)
