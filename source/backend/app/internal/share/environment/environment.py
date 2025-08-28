import os
from dotenv import load_dotenv

load_dotenv()


class Environment:
    """
    環境変数を管理する定数クラス
    """

    # 共通
    APP_ENV: str = os.getenv("APP_ENV", "")
    APP_FRONTEND_URL: str = os.getenv("APP_FRONTEND_URL", "")

    # データベース関連
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    DATABASE_URL_TEST: str = os.getenv("DATABASE_URL_TEST", "")

    # Redis関連
    REDIS_URL: str = os.getenv("REDIS_URL", "")

    # シークレットキー
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")

    # AWS関連
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "")
    AWS_DEFAULT_REGION: str = os.getenv("AWS_DEFAULT_REGION", "")
    AWS_SES_ENDPOINT: str = os.getenv("AWS_SES_ENDPOINT", "")
    AWS_SES_FROM_ADDRESS: str = os.getenv("AWS_SES_FROM_ADDRESS", "")

    # Slack関連
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL", "")
