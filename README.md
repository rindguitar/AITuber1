# プロジェクト名

AITuberKit

## 概要

このプロジェクトは、書籍「AITuberを作ってみたらプロンプトエンジニアリングがよくわかった件」を基に開発した、AITuberを始めるためのキットです。
機能は主に3つあります。

1. キャラクターによるX(旧Twitter)への投稿
2. キャラクターの一日の出来事を生成、日記にし、はてなブログへ投稿
3. キャラクターによる、YouTube配信でのコメントへの返答　現在未実装

## 開発環境

- OS: Windows10
- Python: 3.13.0

## インストール方法

インストール方法を書いてください。
以下のようなコマンドを書くなどすると手順がわかりやすくなるでしょう。

```
make install
```

## 使い方

1. OpenAIのAPIキー、XのConsumerKeysのAPIキー、XのConsumerKeysのAPIキーSecret、
XのBearerToken、XのAccessToken、XのAccessTokenSecret、はてなアカウントのID、
はてなのルートエンドポイントのURL、はてなのAPIキーを取得。

2. .envファイルを下記のように作成。
※ ダブルクォーテーション内に、1.で取得したものをそれぞれ書き込んでください。
```
OPENAI_API_KEY="OpenAIのAPIキー"
Client_ID=""
Client_Secret=""
CONSUMER_KEY="XのConsumerKeysのAPIキー"
CONSUMER_SECRET="XのConsumerKeysのAPIキーSecret"
BEARER_TOKEN="XのBearerToken"
ACCESS_TOKEN="XのAccessToken"
ACCESS_TOKEN_SECRET="XのAccessTokenSecret"
HATENA_ID="はてなアカウントのID"
HATENA_BLOG_ID="はてなのルートエンドポイントのURL"
HATENA_KEY="はてなのAPIキー"
```

3. ディレクトリdocs内の、Character settingをはじめとした全てのファイルの内容を、既述を基に自分の好きなように編集。
※ daily_things_words内のファイルの名称を変更した際は、一部コードの書き換えが必要になります。
例： daily_things_maker.py
     ```
     def load_random_events() -> list[Event]:
            event_list = [
        {"file_name": "home_to_gym", "place": "家→ジム"},
        {"file_name": "gym", "place": "ジム"},
        {"file_name": "gym_to_bar", "place": "ジム→バー"},
        {"file_name": "bar", "place": "バー"},
        {"file_name": "bar_to_home", "place": "バー→家"},
        {"file_name": "home", "place": "家"}
        ]
     ```

4. あとはコードを実行するのみ！
※ コード内に、そのコードの概要説明を記載しております。

## その他
