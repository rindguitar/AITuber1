# プロジェクト名

AITuberKit

## 概要

このプロジェクトは、書籍「AITuberを作ってみたらプロンプトエンジニアリングがよくわかった件」を基に開発した、AITuberを始めるためのキットです。  
機能は主に3つあります。

1. キャラクターによるX(旧Twitter)への投稿
2. キャラクターの一日の出来事を生成、日記にし、はてなブログへ投稿
3. キャラクターによる、YouTube配信でのコメントへの返答

## 開発環境

- OS: Windows10
- Python: 3.13.0

## インストール方法

1. リポジトリをローカルにクローンしてください。
```
git clone https://github.com/rindguitar/AITuber1.git
```
2. ファイルを開いてください。
```
cd AITuber1
```
3. パッケージのインストールをしてください。
```
$ pip install -r requirements.txt
```
完了したら下記の使い方に従い、使用を始めてください。

## 使い方

1. 下記のAPIキーなどを取得。
- OpenAIのAPIキー
- XのConsumerKeysのAPIキー
- XのConsumerKeysのAPIキーSecret
- XのBearerToken
- XのAccessToken
- XのAccessTokenSecret
- はてなアカウントのID
- はてなのルートエンドポイントのURL
- はてなのAPIキー
- OBSのサーバーパスワード
- OBSのサーバーポート
- YouTube配信のVideoID　配信を変えるごとに都度変化。

2. .envファイルを下記のように作成。  
※ ダブルクォーテーション内に、1.で取得したものをそれぞれ書き込んでください。
```
OPENAI_API_KEY="OpenAIのAPIキー"
CONSUMER_KEY="XのConsumerKeysのAPIキー"
CONSUMER_SECRET="XのConsumerKeysのAPIキーSecret"
BEARER_TOKEN="XのBearerToken"
ACCESS_TOKEN="XのAccessToken"
ACCESS_TOKEN_SECRET="XのAccessTokenSecret"
HATENA_ID="はてなアカウントのID"
HATENA_BLOG_ID="はてなのルートエンドポイントのURL"
HATENA_KEY="はてなのAPIキー"
OBS_WS_PASSWORD="OBSのサーバーパスワード"
OBS_WS_HOST="localhost"
OBS_WS_PORT="OBSのサーバーポート"
YOUTUBE_VIDEO_ID="配信のVideoID"
```

3. docsディレクトリ内の、Character settingをはじめとした全てのファイルの内容を、既述を基に自分の好きなように編集。  
※ daily_things_words内のファイルの名称を変更した際は、一部コードの書き換えが必要になります。  
例： src/diary/daily_things_maker.py

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
4. あとはプログラムを実行するのみ！  
※ プログラム内に、そのプログラムの概要説明を記載しております。

## その他

tweet_themeはCharacter settingをLLMに入力し、出力を手伝ってもらうことをオススメします。

daily_things_words内のファイルには、一日の時系列でキャラクターがいそうな場所を定義し、  
その場所ごとで起こりそうな出来事やキャラクターの思考、言動をLLMに単語や短文で出力してもらったものを記載してください。
  
私はプログラムを書いてまとめただけなので細かな意図などは、書籍「AITuberを作ってみたらプロンプトエンジニアリングがよくわかった件」を読んでいただけると分かると思います。