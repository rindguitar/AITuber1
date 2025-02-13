.PHONY: build run help

default: help

build:  ## Dockerイメージをビルド
	docker build -t aituberkit .

run:  ## Dockerコンテナを起動
	docker run -it aituberkit

help:  ## ヘルプ
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'