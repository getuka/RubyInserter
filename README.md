
# Rubyinserter

**Rubyinserter** は、日本語の漢字にルビ（ふりがな）を挿入するためのPythonライブラリです。日本語テキストにルビ（ふりがな）を挿入し、TTSモデルの発音を安定させます。

- 日本語の漢字に自動的にルビ（ふりがな）を生成します。
- Pythonプロジェクトに簡単に統合可能です。
- カスタマイズや複数のテキスト処理オプションをサポートします。

## インストール

Rubyinserterをインストールするには、以下のコマンドを使用してください

```bash
pip install git+https://github.com/yourusername/rubyinserter.git
```

## 使用方法

Rubyinserterの基本的な使用例

```python
from rubyinserter import add_ruby_text

text = "石炭の積み込みがもう終わった。"
ruby_text = add_ruby_text(text)
print(ruby_text)
```

出力：

```
石炭[せきたん]の積み込み[つみこみ]がもう終わっ[おわっ]た。
```


## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については [LICENSE](LICENSE) ファイルをご覧ください。
