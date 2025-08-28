###############################################
# ビルドステージ
###############################################
FROM python:3.12-slim AS base

# 環境変数の設定
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH /usr/src/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPYCACHEPREFIX=/var/cache/python

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y curl \
 && curl -LsSf https://astral.sh/uv/install.sh | sh \
 && rm -rf /var/lib/apt/lists/*

# ワークディレクトリの指定
WORKDIR /usr/src/app

# ソースコードをコンテナにコピー
COPY ../../source/backend /usr/src/app

###############################################
# 開発用ステージ
###############################################
FROM base AS dev

# モジュールのインストール
RUN uv pip install --system -e . --group dev

# アプリケーションの起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

###############################################
# 本番用ステージ
###############################################
FROM base AS prod

# モジュールのインストール
RUN uv pip install --system -e .

# アプリケーションの起動
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
