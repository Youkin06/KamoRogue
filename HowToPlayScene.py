import pyxel
import PyxelUniversalFont as puf

class HowToPlayScene:
    def __init__(self):
        self.writer = puf.Writer("misaki_gothic.ttf")

    def update(self):
        # Press Enter to proceed to Game
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
        
        # Draw Background (Tilemap 0, Start x=0, y=16)
        base_ty = 16
        for ty in range(15):
            for tx in range(20):
                tile = pyxel.tilemaps[0].pget(tx, base_ty + ty)
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16, ty * 16, 1, src_x, src_y, 8, 8, 0, scale=2.0)
        
        # --- Title ---
        title = "OPERATION"
        # Size 16 used in AbilitySelect for Title
        self.writer.draw(120, 20, title, 16, 7)
        
        # --- Main Image ---
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
        
        # Center the main image logic
        draw_x = cx - draw_w / 2
        draw_y = 60 # Adjusted Y to fit everything
        
        pyxel.blt(draw_x + 20, draw_y, 0, img_u, img_v, img_w, img_h, 0, scale=scale)
        
        # --- Keys ---
        # WAD (Left side) -> Using AD Key sprite as placeholder (u=0, v=96, w=21, h=13)
        key_scale = 2.0
        wad_w = 21 * key_scale
        wad_h = 13 * key_scale
        
        # JK (Right side) -> Using Enter Key sprite as placeholder (u=48, v=96, w=25, h=13)
        jk_w = 25 * key_scale
        jk_h = 13 * key_scale
        
        # Align keys vertically with the bottom part of the main image or centered?
        # User said "Left side WAD, Right side JK".
        keys_y = draw_y + draw_h - wad_h # Align bottom
        
        # Draw WAD (AD sprite)
        #pyxel.blt(draw_x - wad_w - 10, keys_y, 0, 0, 96, 21, 13, 0, scale=key_scale)
        
        # Draw JK (Enter sprite)
        ##pyxel.blt(draw_x + draw_w + 10, keys_y, 0, 48, 96, 25, 13, 0, scale=key_scale)
        
        # --- Description (Japanese) ---
        y_text = 130
        lines = [
            "Wキー: ジャンプ",
            "ADキー: 左右移動",
            "Jキー: ショット",
            "Kキー: ガード(アビリティがあるとき)"
        ]
        
        for i, line in enumerate(lines):
            # Centering
            # Use size 8 (AbilitySelect description size)
            lw = self.get_text_width(line) # get_text_width assumes size 8 (4px/8px) logic
            lx = cx - lw / 2
            self.writer.draw(lx, y_text + i * 16, line, 8, 7)
            
        # --- Press Enter ---
        msg = "PRESS ENTER TO START"
        mw = len(msg) * 8 # Approximation for large font? 
        # Actually puf handles drawing. If we use size 8, width is roughly len*something.
        # Let's center manually or guess. 
        # "PRESS ENTER TO START" is ~20 chars. 20 * 8 = 160.
        #self.writer.draw(160, 210, msg, 8, 7)

        #Enterキー
        pyxel.blt(140 + 120, 200-8 -20, 0, 48, 96, 25, 13, 0, scale=2.0)
        #CONFILM文字
        pyxel.blt(140 + 120, 232-8 -20, 0, 23, 102, 18+6, 5, 0, scale=2.0)
