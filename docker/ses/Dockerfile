FROM node:18

# ワークディレクトリの指定
WORKDIR /app

# aws-ses-v2-localのインストール
RUN npm install -g aws-ses-v2-local

# エントリーポイントの指定
ENTRYPOINT ["aws-ses-v2-local", "--host=0.0.0.0"]