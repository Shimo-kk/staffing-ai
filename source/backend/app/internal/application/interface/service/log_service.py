from abc import ABC, abstractmethod


class ILogService(ABC):
    """
    ログサービスのインターフェース
    """

    @abstractmethod
    def debug(self, message: str, **kwargs) -> None:
        """
        デバッグレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        ...

    @abstractmethod
    def info(self, message: str, **kwargs) -> None:
        """
        情報レベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        ...

    @abstractmethod
    def warning(self, message: str, **kwargs) -> None:
        """
        警告レベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        ...

    @abstractmethod
    def error(self, message: str, **kwargs) -> None:
        """
        エラーレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        ...

    @abstractmethod
    def critical(self, message: str, **kwargs) -> None:
        """
        致命的エラーレベルのログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def exception(self, message: str, **kwargs) -> None:
        """
        例外情報を含むログを出力する

        Args:
            message (str): ログメッセージ
            **kwargs: 追加のコンテキスト情報（request_id, protocol, host, url, method, status, stack等）

        Returns:
            None
        """
        ...

    @abstractmethod
    def set_level(self, level: int) -> None:
        """
        ログレベルを設定する

        Args:
            level (int): 設定するログレベル（logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL）

        Returns:
            None
        """
        ...
