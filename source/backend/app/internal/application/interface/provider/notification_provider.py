from abc import ABC, abstractmethod


class INotificationProveider(ABC):
    """
    通知機能を提供するプロバイダのインターフェースクラス
    """

    @abstractmethod
    async def notify_error(self, request_id: str, exception: Exception):
        """
        エラーを通知する

        Args:
            request_id (str): リクエストID
            exception (Exception): 発生した例外

        Returns:
            None
        """
        ...
