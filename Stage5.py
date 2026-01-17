import pyxel
import Stage
import Enemy1
import Enemy3
import Enemy2
import Toge

class Stage5(Stage.Stage):
    def __init__(self):
        super().__init__()
        # Stage4の設定またはデフォルトをベースに使用。ユーザーはStage5の内容を指定していない。
        # とりあえずシンプルにする。
        
        self.limit_x_min = 0 # デフォルト
        self.limit_x_max = 144 # デフォルト
        
        self.player_start_x = 16
        self.player_start_y = 88
        
        # デフォルトの衝突タイルを追加するか、空/最小限のままにする
        self.collision_tiles = [(89 -80,8*8), (90 -80,8*8),(91 -80,8*8)] 
        
        # とりあえずダミーの敵を追加するか？それとも空のままにする？
        # 通常、テストの「クリア」ロジックのために1体の敵がいると良いが、
        # ユーザーは単に「Stage5を作成」とだけ言った。
        # シンプルな敵を1体追加する。
        self.enemies.append(Enemy3.Enemy3(80, 88, 80, 120))

    def draw(self):
        # Stage1/Testの描画ロジック（タイルマップ）を再利用
        for ty in range(15): 
            for tx in range(20): 
                tile = pyxel.tilemaps[0].pget(tx + 80, ty) # +80のオフセット
                src_x = tile[0] * 8
                src_y = tile[1] * 8
                pyxel.blt(tx * 16 + 4, ty * 16 + 4, 1, src_x, src_y, 8, 8, 0, scale=2.0)

        super().draw()
