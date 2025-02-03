import feedparser
import requests
from requests.auth import HTTPBasicAuth
import dotenv
import os


class BlogUtils:
    def __init__(self):
        dotenv.load_dotenv()

        self.hatena_id = os.getenv("HATENA_ID")
        self.blog_id = os.getenv("HATENA_BLOG_ID")
        self.url = f"https://blog.hatena.ne.jp/{self.hatena_id}/{self.blog_id}.hatenablog.com/atom"
        self.key = os.getenv("HATENA_KEY")
        
        # /entryエンドポイントを使用してデータを取得するための変数を設定
        self.endpoint = "/entry"
        self.req_endpoint = f"{self.url}{self.endpoint}"
        # test_post_data.xmlを読み込む
        with open('config/test_post_data.xml', 'r', encoding='utf-8') as file:
            self.data = file.read()

    def read_latest_blog(self)->str:
        # POSTリクエストを送信
        response = requests.post(
            self.req_endpoint,
            auth=HTTPBasicAuth(username=self.hatena_id, password=self.key),
            headers={'Content-Type': 'application/xml'},
            data=self.data
        )
        try:
            if response.status_code == 200:
                print("レスポンスは正常です")
            else:
                print(f'Failed to post: {response.status_code}')
                exit(1)
            
            #レスポンスのXMLをパースして、記事のタイトルとURLを取得
            feed = feedparser.parse(response.text)
        
            # ブログの最新の投稿の内容を取得
            entry = feed.entries[0]
            return entry.content[0].value
        
        except Exception as e:
            print(f'Failed to post: {response.status_code}')
            raise e
        
        