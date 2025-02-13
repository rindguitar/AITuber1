# ベースイメージ
FROM python:3.13.0-slim

# 作業ディレクトリを指定
WORKDIR /app

# 必要なライブラリをrequirements.txtからインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# コードコピー
# 今回はすべてのファイルをコピーすることにする、本来は必要なファイルだけコピーすべき
COPY . .

# TODO(これから何をするか？):
# 認証情報やAPIキーなどをDockerコンテナに渡す
# GitHubのリポジトリに認証キーなどのセンシティブな情報をpushしないように注意！
# いくつかの方法があり得るので、調べてみてください

# コマンドを実行、今回はシェルを実行することにする
CMD ["/bin/bash"]