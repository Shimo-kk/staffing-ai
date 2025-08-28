import logging
import logging.config
from app.internal.share.config.logging import logging_config
from app.internal.application.interface.service.log_service import ILogService


class LogService(ILogService):
    """
    ログサービスの実装クラス
    """

    def __init__(self):
        logging.config.dictConfig(logging_config)

        self._logger = logging.getLogger(__name__)

    def debug(self, message: str, **kwargs) -> None:
        """
        デバッグレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.debug(message, extra=kwargs)

    def info(self, message: str, **kwargs) -> None:
        """
        情報レベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.info(message, extra=kwargs)

    def warning(self, message: str, **kwargs) -> None:
        """
        警告レベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.warning(message, extra=kwargs)

    def error(self, message: str, **kwargs) -> None:
        """
        エラーレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.error(message, extra=kwargs)

    def critical(self, message: str, **kwargs) -> None:
        """
        致命的エラーレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.critical(message, extra=kwargs)

    def exception(self, message: str, **kwargs) -> None:
        """
        例外情報を含むログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        self._logger.exception(message, extra=kwargs)

    def set_level(self, level: int) -> None:
        """
        ログレベルを設定する

        Args:
            level (int): 設定するログレベル（logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL）

        Returns:
            None
        """
        self._logger.setLevel(level)
