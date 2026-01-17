
import pyxel
import sys

class App:
    def __init__(self):
        pyxel.init(160, 120, display_scale=1) # 最小ウィンドウ
        pyxel.images[0].set(0, 0, ["00000000", "00000000", "00111100", "01000010", "01000010", "00111100", "00000000", "00000000"])
        # 1フレーム実行して終了
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.frame_count > 0:
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        try:
            pyxel.blt(10, 10, 0, 0, 0, 8, 8, 0, scale=2.0)
            print("SCALE_SUPPORTED")
        except TypeError:
            print("SCALE_NOT_SUPPORTED")
        except Exception as e:
            print(f"ERROR: {e}")

App()
