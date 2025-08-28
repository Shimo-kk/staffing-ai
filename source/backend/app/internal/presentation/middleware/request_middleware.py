from fastapi import Request, Response, status, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from uuid import uuid4
import traceback
from app.internal.dependency_injector import dependency_injector
from app.internal.application.interface.provider.log_provider import ILogProvider
from app.internal.application.interface.provider.notification_provider import (
    INotificationProveider,
)


class RequestMiddleware(BaseHTTPMiddleware):
    """
    HTTPリクエストを処理するミドルウェア
    """

    def __init__(self, app):
        """
        コンストラクタ
        """
        super().__init__(app)

        self._log_provider: ILogProvider = dependency_injector.get(ILogProvider)
        self._notification_provider: INotificationProveider = dependency_injector.get(
            INotificationProveider
        )

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        ミドルウェアの処理

        Args:
            request (Request): リクエスト情報
            call_next (method): 次の処理

        Returns:
            Response: レスポンス
        """

        # リクエストIDを生成
        request_id = str(uuid4())

        # リクエストログを出力
        self._log_provider.request_log(
            request_id=request_id,
            protocol=request.url.scheme,
            host=request.url.hostname or "unknown",
            url=str(request.url.path),
            method=request.method,
        )

        try:
            # 次の処理を実行
            response = await call_next(request)

            # レスポンスログを出力
            self._log_provider.responce_log(
                request_id=request_id, status=response.status_code
            )

            return response
        except HTTPException as e:
            # レスポンスログを出力
            self._log_provider.responce_log(
                request_id=request_id, status=e.status_code, detail=str(e.detail)
            )

            return JSONResponse(
                {
                    "detail": e.detail,
                },
                status_code=e.status_code,
            )
        except Exception as e:
            # エラーログを出力
            self._log_provider.error_log(
                name=type(e).__name__, stack=traceback.format_exc()
            )

            # レスポンスログを出力
            self._log_provider.responce_log(
                request_id=request_id, status=500, detail=str(e)
            )

            # エラーを通知
            await self._notification_provider.notify_error(
                request_id=request_id, exception=e
            )

            return JSONResponse(
                {
                    "detail": str(e),
                },
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
