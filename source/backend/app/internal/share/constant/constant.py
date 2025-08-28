class Constants:
    """
    アプリケーション全体で利用する定数を管理するクラス
    """

    # 環境
    APP_ENV_DEV: str = "dev"
    APP_ENV_PROD: str = "prod"

    # セッション有効期限
    SESSION_EXPIRE: int = 86400

    # CSRF有効期限
    CSRF_EXPIRE: int = 7200

    # ロール
    ROLE_OWNER: int = 1
    ROLE_ADMIN: int = 2
    ROLE_GENERAL: int = 3
    ROLE_STAFF: int = 4

    # ライフサイクル
    LIFECYCLE_ACTIVE: int = 1
    LIFECYCLE_SUSPENDED: int = 2
