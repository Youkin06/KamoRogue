import pyxel
import PyxelUniversalFont as puf

class AbilitySelectScene:
    def __init__(self):
        self.writer = puf.Writer("misaki_gothic.ttf")

        self.selected_index = 0
        self.options = []
        self.player = None

    def set_options(self, options, player):
        self.options = options
        self.player = player
        self.selected_index = 0

    def update(self):
        max_index = max(0, len(self.options) - 1)
        
        if pyxel.btnp(pyxel.KEY_A):
            self.selected_index -= 1
            if self.selected_index < 0:
                self.selected_index = 0
                
        if pyxel.btnp(pyxel.KEY_D):
            self.selected_index += 1
            if self.selected_index > max_index:
                self.selected_index = max_index
                
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.options and self.player:
                selected_ability = self.options[self.selected_index]
                print(selected_ability.name)
                selected_ability.apply(self.player)
                return True
        return False

    def get_text_width(self, text):
        width = 0
        for char in text:
            if ord(char) < 256:
                width += 4
            else:
                width += 8
        return width

    def draw(self):
        self.writer.draw(105, 40, "ABILITY SELECT", 16, 7)
        
        # 選択肢の数に基づいてボックス位置を定義
        box_positions = []
        num_options = len(self.options)
        
        if num_options == 1:
            box_positions = [(64, 30)] # 中央
        elif num_options == 2:
            box_positions = [(40, 30), (88, 30)] # 中央揃えペア
        else:
            box_positions = [(16, 30), (64, 30), (112, 30)] # 標準3つ
        
        # ボックス描画
        for i, pos in enumerate(box_positions):
            # 座標を2倍にスケーリング
            x, y = pos
            draw_x = x * 2
            draw_y = y * 2
            
            # ボックス描画 (32x32 -> スケール2.0 -> 64x64) オフセット +16
            pyxel.blt(draw_x + 16, draw_y + 16, 0, 0, 64, 32, 32, 0, scale=2.0)
            
            # 選択されている場合ハイライト描画
            if i == self.selected_index:
                # スプライトハイライト描画 (32, 64) サイズ 32x32 -> スケール2.0 オフセット +16
                pyxel.blt(draw_x + 16, draw_y + 16, 0, 32, 64, 32, 32, 0, scale=2.0)

            # アビリティアイコン描画 (選択肢が存在する場合)
            if i < len(self.options):
                ability = self.options[i]
                # アイコンをボックスの中央に配置 (元オフセット8 -> スケール後16)
                # アイコン W=16 -> オフセット +8
                # 位置: draw_x + 16. オフセット込み: draw_x + 16 + 8 = draw_x + 24
                pyxel.blt(draw_x + 24, draw_y + 24, 0, ability.u, ability.v, 16, 16, 0, scale=2.0)
                
                # アビリティ名描画 (y=66 -> 132)
                name = ability.name
                # 中央揃え
                name_width = self.get_text_width(name)
                name_draw_x = draw_x + 32 - (name_width // 2)
                self.writer.draw(name_draw_x, 132, name, 8, 7)
                
                # アビリティ説明描画 (y=74 -> 148)
                desc = ability.description
                for i, line in enumerate(desc.split('\n')):
                    line_width = self.get_text_width(line)
                    desc_draw_x = draw_x + 32 - (line_width // 2)
                    self.writer.draw(desc_draw_x, 148 + i * 10, line, 8, 7)

        # 操作説明描画 (y=100 -> 200)
        # 左コントロール W=16 -> オフセット +8
        #pyxel.blt(80 + 8, 200 + 8, 0, 32, 96, 16, 16, 0, scale=2.0)
        #pyxel.blt(112 + 8, 200 + 8, 0, 0, 96, 16, 16, 0, scale=2.0)
        
        # 右コントロール
        #pyxel.blt(176 + 8, 200 + 8, 0, 16, 96, 16, 16, 0, scale=2.0)
        #pyxel.blt(208 + 8, 200 + 8, 0, 32, 96, -16, 16, 0, scale=2.0)

        #ADキー
        pyxel.blt(140, 200-8, 0, 0, 96, 20+1, 13, 0, scale=2.0)
        # SELECT文字
        pyxel.blt(139, 232-8, 0, 23, 96, 18+6, 5, 0, scale=2.0)
        #Enterキー
        pyxel.blt(140 + 120, 200-8, 0, 48, 96, 25, 13, 0, scale=2.0)
        #CONFILM文字
        pyxel.blt(140 + 120, 232-8, 0, 23, 102, 18+6, 5, 0, scale=2.0)
        