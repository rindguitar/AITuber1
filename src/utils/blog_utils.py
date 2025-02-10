# はてなの最新記事を取得するプログラム

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
            
    def read_latest_blog(self) -> str:
        # GETリクエストを送信
        response = requests.get(self.req_endpoint,
                                auth=HTTPBasicAuth(self.hatena_id, self.key),
                                headers={'Content-Type': 'application/xml'})
        try:
            
            if response.status_code == 200:
                print("ok")
            else:
                print(f'Failed to post: {response.status_code}')
                exit(1)    
        
            
            # レスポンスのXMLをパースして、記事のタイトルとURLを取得
            feed = feedparser.parse(response.text)
            
            # ブログの最新の投稿の内容を取得
            entry = feed.entries[0]
            return entry.content[0].value
        
        except Exception as e:
            print(f'Failed to post: {response.status_code}')
            raise e

if __name__ == "__main__":
    blog_utils = BlogUtils()
    print(blog_utils.read_latest_blog())