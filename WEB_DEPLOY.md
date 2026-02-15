# Web公開手順 (Pyxel)

## 1. ビルド

```bash
./.venv/bin/pyxel package . App.py
./.venv/bin/pyxel app2html MyGame.pyxapp
```

生成物:
- `MyGame.pyxapp`
- `MyGame.html` (単一HTML。公開時の推奨)
- `index.html` (ランチャー方式)

## 2. 配置

### 推奨 (単一HTML)

`MyGame.html` を GitHub Pages の `index.html` として配置してください。  
（`MyGame.pyxapp` の配置ミスやキャッシュ問題を避けやすい）

### ランチャー方式を使う場合

同じディレクトリに以下を置いて公開してください。
- `index.html`
- `MyGame.pyxapp`
- `pyxel.js` (任意。あるとCDN障害時も起動可能)

※ `pyxel.js` がない場合は `index.html` がCDNから取得します。

## 3. ローカル確認

```bash
python3 -m http.server 8000
```

ブラウザで `http://localhost:8000/index.html` を開く。

## 日本語フォント対策

このプロジェクトは `misaki_gothic.ttf` を `PyxelUniversalFont` から参照しています。
Webで壊れやすいポイントは「フォントを外部環境に依存して読む」ことです。

対策として、以下を実施済みです。
- `PyxelUniversalFont` をプロジェクト内に同梱
- `PyxelUniversalFont/fonts/misaki_gothic.ttf` を同梱

これにより、`pyxel package` 時にフォントが `MyGame.pyxapp` に内包され、
配信先OSのフォント有無や外部URLに依存しにくくなります。

## 補足

`PyxelUniversalFont` は `Pillow` / `numpy` を使うため、環境依存が残る可能性があります。
将来的にさらに安定させるなら、
- BDFビットマップフォント + `pyxel.Font` へ移行
- または日本語テキストを画像化して `blt` 描画

が最も堅いです。
