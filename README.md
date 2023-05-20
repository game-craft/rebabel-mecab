# rebabel-mecab
Re:babelのMeCabを使用した形態素解析用API。
## 環境構築
1.コンテナを起動
```
docker compose up -d --build
```
2.コンテナに入る
```
docker container exec -it rebabel-mecab-app-1 bash
```
5.サーバーを起動
```
uvicorn main:APP --host=0.0.0.0 --port=8000
```
