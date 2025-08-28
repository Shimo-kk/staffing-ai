from injector import inject
from app.internal.application.interface.provider.log_provider import ILogProvider
from app.internal.application.interface.service.log_service import ILogService


class LogProvider(ILogProvider):
    """
    ログ機能を提供するプロバイダーの実装クラス
    """

    @inject
    def __init__(self, log_service: ILogService):
        """
        コンストラクタ
        """
        self._log_service = log_service

    def request_log(
        self,
        request_id: str,
        protocol: str,
        host: str,
        url: str,
        method: str,
        detail: str = "",
    ):
        """
        リクエストログを出力する

        Args:
            request_id (str): リクエストID
            protocol (str): プロトコル（http, https等）
            host (str): ホスト名
            url (str): リクエストURL
            method (str): HTTPメソッド（GET, POST等）
            detail (str): 詳細

        Returns:
            None
        """
        kwargs = {
            "request_id": request_id,
            "protocol": protocol,
            "host": host,
            "url": url,
            "method": method,
            "detail": detail,
        }
        # Noneや空文字列の値を除外
        kwargs = {k: v for k, v in kwargs.items() if v is not None and v != ""}

        self._log_service.info("Request received", **kwargs)

    def responce_log(self, request_id: str, status: int, detail: str = ""):
        """
        レスポンスログを出力する

        Args:
            request_id (str): リクエストID
            status (int): HTTPステータスコード
            detail (str): 詳細

        Returns:
            None
        """
        kwargs = {
            "request_id": request_id,
            "status": status,
            "detail": detail,
        }
        # Noneや空文字列の値を除外
        kwargs = {k: v for k, v in kwargs.items() if v is not None and v != ""}

        self._log_service.info("Response sent", **kwargs)

    def error_log(self, name: str, stack: str):
        """
        エラーログを出力する

        Args:
            name (str): エラー名
            stack (str): スタックトレース

        Returns:
            None
        """
        kwargs = {"error_name": name, "error_stack": stack}
        # Noneや空文字列の値を除外
        kwargs = {k: v for k, v in kwargs.items() if v is not None and v != ""}

        self._log_service.error(f"Error occurred: {name}", **kwargs)
