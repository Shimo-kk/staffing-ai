from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.internal.share.config.database import (
    AsyncSessionLocal,
    set_session,
    reset_session,
)


class DBSessionMiddleware(BaseHTTPMiddleware):
    """
    HTTPリクエストごとにDBセッションを管理するミドルウェア
    """

    async def dispatch(self, request: Request, call_next):
        """
        ミドルウェアの処理

        Args:
            request (Request): リクエスト情報
            call_next (method): 次の処理

        Returns:
            Response: レスポンス
        """

        async with AsyncSessionLocal() as session:
            try:
                token = set_session(session)
                response = await call_next(request)
                await session.commit()
                return response
            except Exception:
                await session.rollback()
                raise
            finally:
                reset_session(token)
