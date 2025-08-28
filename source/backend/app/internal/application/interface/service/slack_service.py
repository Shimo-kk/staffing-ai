from abc import ABC, abstractmethod


class ISlackService(ABC):
    """
    Slackと連携するサービスのインターフェースクラス
    """

    @abstractmethod
    async def notify(self, message: str, channel_mention: bool = False):
        """
        Slackへ通知する

        Args:
            message (str): ログメッセージ
            channel_mention (bool): チャンネル全体にメンションするかどうか（デフォルト: False）

        Returns:
            None
        """
        ...
