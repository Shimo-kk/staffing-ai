import httpx
from app.internal.application.interface.service.slack_service import ISlackService
from app.internal.share.environment.environment import Environment


class SlackService(ISlackService):
    """
    Slackと連携するサービスの実装クラス
    """

    def __init__(self):
        """
        コンストラクタ
        """
        pass

    async def notify(self, message: str, channel_mention: bool = False) -> None:
        """
        Slackへ通知する

        Args:
            message (str): ログメッセージ
            channel_mention (bool): チャンネル全体にメンションするかどうか（デフォルト: False）

        Returns:
            None
        """
        if Environment.SLACK_WEBHOOK_URL == "":
            return

        # チャンネルメンションが有効な場合は、メッセージの先頭に<!here>を追加
        if channel_mention:
            message = "<!here> " + message

        payload = {"text": message}

        async with httpx.AsyncClient() as client:
            try:
                await client.post(Environment.SLACK_WEBHOOK_URL, json=payload)
            except httpx.TimeoutException:
                print("slack notification timeout")
