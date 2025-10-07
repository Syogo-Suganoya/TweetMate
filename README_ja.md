[For English](https://github.com/Syogo-Suganoya/TweetMate/blob/main/README.md)

# オモイアイ - 共通点発見ツール

## 概要

このツールは、X（旧Twitter）の投稿から共通のキーワードを抽出し、ユーザー間の共通点を見つけるためのプログラムです。日本語のストップワードを除外し、自然言語処理を用いて共通トピックを抽出します。

---

## 主な機能

1. **投稿データ取得**
   - X API またはモックデータを使用して、指定されたユーザーの投稿を取得します。
2. **共通キーワード抽出**
   - TinySegmenter を使用して日本語のトークン化を行い、ストップワードを除外した共通キーワードを抽出します。
3. **モックデータ対応**
   - 実データの代わりにモックデータを使用して動作確認が可能です。

---

## 使用技術

- **Pythonライブラリ**
  - `dotenv`: 環境変数の読み込み
  - `tinysegmenter`: 日本語トークン化
  - `argparse`: コマンドライン引数の解析
  - `urllib`: 外部リソースの取得

- **外部リソース**
  - [stopwords-ja](https://github.com/stopwords-iso/stopwords-ja): 日本語ストップワードリスト

---

## インストール

1. 必要なライブラリをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

2. 環境変数を設定します。`.env` ファイルを作成し、以下の内容を記載してください。

    ```env
    X_API_KEY="YOUR_X_API_KEY"
    X_API_KEY_SECRET="YOUR_X_API_KEY_SECRET"
    X_ACCESS_TOKEN="YOUR_X_ACCESS_TOKEN"
    X_ACCESS_TOKEN_SECRET="YOUR_X_ACCESS_TOKEN_SECRET"
    ```

---

## 実行方法

### 実データを使用する場合

以下のコマンドを実行します。

```bash
python main.py --user1 <ユーザー1のID> --user2 <ユーザー2のID>
```

例:

```bash
python main.py --user1 "user1_id" --user2 "user2_id"
```

### モックデータを使用する場合

以下のコマンドを実行します。

```bash
python main.py --mock
```

---

## 注意事項

- X API を使用する場合、APIキーを正しく設定してください。
- モックデータを使用する場合、`--user1` や `--user2` を指定しないでください。

---

## 課題と今後の展望

- **日本語トークン化の改善**
  - 現在は TinySegmenter を使用していますが、より精度の高いトークン化ツール（例: MeCab, GiNZA）への移行を検討しています。

- **Web UI の実装**
  - コマンドラインツールから Web アプリケーションへの拡張を予定しています。

- **感情分析の導入**
  - 共通キーワードの感情的なニュアンスを分析し、より深い洞察を提供します。
