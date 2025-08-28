from injector import inject
from app.internal.application.interface.provider.notification_provider import (
    INotificationProveider,
)
from app.internal.application.interface.service.slack_service import ISlackService


class NotificationProvider(INotificationProveider):
    """
    通知機能を提供するプロバイダの実装クラス
    """

    @inject
    def __init__(self, slack_service: ISlackService):
        """
        コンストラクタ
        """
        self._slack_service = slack_service

    async def notify_error(self, request_id: str, exception: Exception):
        """
        エラーを通知する

        Args:
            request_id (str): リクエストID
            exception (Exception): 発生した例外

        Returns:
            None
        """
        message = f"エラーが発生しました。\n\nリクエストID: {request_id}\nエラー内容: {type(exception).__name__}\nメッセージ: {str(exception)}"
        await self._slack_service.notify(message)
