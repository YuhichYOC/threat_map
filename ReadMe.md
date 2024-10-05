### threat_map by Yuichi Yoshii is licensed under the Apache License, Version2.0

# セットアップ及び利用方法

## 0. 確認済み動作環境
- Ubuntu 24.04
- WSL2 Ubuntu

## 1. 事前準備

### 1-1. シークレットキーの用意
django をインストール済みの仮想環境で django.core.management.utils.get_random_secret_key を呼び出し、シークレットキーを生成  
```bash
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'p7_dz!@8r0sj(za4xk_@d#1zun4k0eecz#4p6pw*s2dx@0%)l%'
```

- p7_dz!@8r0sj(za4xk_@d#1zun4k0eecz#4p6pw*s2dx@0%)l% がシークレットキーです。シングルクォートは外して利用します

### 1-2. Google maps API キーの用意

自分は以下の記事を参考にしました  
[Google Mapのキーの取得方法](https://qiita.com/sera_ramon/items/707ac5064f6e6343df05)

## 2. threat_map のクローン
```bash
vmuser1@vm:~$ git clone https://github.com/YuhichYOC/threat_map.git
```

## 3. 環境変数を .env ファイルに記入
```
YOUR_DJANGO_SECRET_KEY=[1-1 で生成したシークレットキーを記入]
YOUR_MAPS_API_KEY=[1-2 で取得した Google maps API キーを記入]
```

## 4. コンテナイメージのビルド
```bash
vmuser1@vm:~/threat_map$ sudo docker build -t yuhichyoc/threat_map:latest .
```

## 5. コンテナ起動
```bash
vmuser1@vm:~/threat_map$ sudo docker run --name threat_map -p 80:80 -dit yuhichyoc/threat_map:latest
```

## 6. Web ブラウザで危険顧客マップを閲覧
http://localhost/ をブラウザで開く
