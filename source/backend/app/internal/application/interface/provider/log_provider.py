from abc import ABC, abstractmethod


class ILogProvider(ABC):
    """
    ログ機能を提供するプロバイダーのインターフェースクラス
    """

    @abstractmethod
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

        Returns:
            None
        """
        ...

    @abstractmethod
    def responce_log(self, request_id: str, status: int, detail: str = ""):
        """
        レスポンスログを出力する

        Args:
            request_id (str): リクエストID
            status (int): HTTPステータスコード

        Returns:
            None
        """
        ...

    @abstractmethod
    def error_log(self, name: str, stack: str):
        """
        エラーログを出力する

        Args:
            name (str): エラー名
            stack (str): スタックトレース

        Returns:
            None
        """
        ...
