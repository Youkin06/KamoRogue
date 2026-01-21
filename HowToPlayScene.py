import pyxel
import PyxelUniversalFont as puf

class HowToPlayScene:
    def __init__(self):
        self.writer = puf.Writer("misaki_gothic.ttf")

    def update(self):
        # Enterキーでゲームへ進む
        if pyxel.btnp(pyxel.KEY_RETURN):
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
        pyxel.cls(0)
        
        # 背景を描画 (タイルマップ 0, 開始 x=0, y=16)
        base_ty = 16
        for ty in range(15):
            for tx in range(20):
                tile = pyxel.tilemaps[0].pget(tx, base_ty + ty)
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16, ty * 16, 1, src_x, src_y, 8, 8, 0, scale=2.0)
        
        # --- タイトル ---
        title = "OPERATION"
        # AbilitySelectのタイトルと同じサイズ16を使用
        self.writer.draw(120, 20, title, 16, 7)
        
        # --- メイン画像 ---
        # Image0 (8, 152) - (63, 178) -> 56x27
        img_u = 8
        img_v = 152
        img_w = 56
        img_h = 27
        
        scale = 2.0
        draw_w = img_w * scale
        draw_h = img_h * scale
        
        cx = 320 / 2
        cy = 240 / 2
        
        # メイン画像の中心配置ロジック
        draw_x = cx - draw_w / 2
        draw_y = 60 # 全体が収まるようにY調整
        
        pyxel.blt(draw_x + 20, draw_y, 0, img_u, img_v, img_w, img_h, 0, scale=scale)
        
        # --- キー ---
        # WAD (左側) -> プレースホルダーとしてADキースプライトを使用 (u=0, v=96, w=21, h=13)
        key_scale = 2.0
        wad_w = 21 * key_scale
        wad_h = 13 * key_scale
        
        # JK (右側) -> プレースホルダーとしてEnterキースプライトを使用 (u=48, v=96, w=25, h=13)
        jk_w = 25 * key_scale
        jk_h = 13 * key_scale
        
        # キーをメイン画像の下部に合わせるか中央に配置するか？
        # ユーザーは「左側にWAD、右側にJK」と言っていた。
        keys_y = draw_y + draw_h - wad_h # 下揃え
        
        # WAD描画 (ADスプライト)
        #pyxel.blt(draw_x - wad_w - 10, keys_y, 0, 0, 96, 21, 13, 0, scale=key_scale)
        
        # JK描画 (Enterスプライト)
        ##pyxel.blt(draw_x + draw_w + 10, keys_y, 0, 48, 96, 25, 13, 0, scale=key_scale)
        
        # --- 説明文 (日本語) ---
        y_text = 130
        lines = [
            "Wキー: ジャンプ",
            "ADキー: 左右移動",
            "Jキー: ショット",
            "Kキー: ガード(アビリティがあるとき)"
        ]
        
        for i, line in enumerate(lines):
            # 中央揃え
            # サイズ8を使用 (AbilitySelectの説明文サイズ)
            lw = self.get_text_width(line) # get_text_widthはサイズ8 (4px/8px) ロジックを想定
            lx = cx - lw / 2
            self.writer.draw(lx, y_text + i * 16, line, 8, 7)
            
        # --- Enterを押す ---
        msg = "PRESS ENTER TO START"
        mw = len(msg) * 8 # 大きなフォントのための概算？
        # 実際にはpufが描画を処理する。サイズ8を使用する場合、幅はおよそ len*something。
        # 手動で中央揃えするか推測する。
        # "PRESS ENTER TO START" は約20文字。20 * 8 = 160。
        #self.writer.draw(160, 210, msg, 8, 7)

        #Enterキー
        pyxel.blt(140 + 120, 200-8 -20 - 15, 0, 48, 96, 25, 13, 0, scale=2.0)
        #CONFILM文字
        pyxel.blt(140 + 120, 232-8 -20 - 15, 0, 23, 102, 18+6, 5, 0, scale=2.0)
