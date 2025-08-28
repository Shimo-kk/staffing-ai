from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from app.internal.presentation.middleware.dbsession_middleware import (
    DBSessionMiddleware,
)
from app.internal.presentation.middleware.request_middleware import RequestMiddleware
from app.internal.share.environment.environment import Environment
from app.router import api_router

app = FastAPI()

# データベースセッションミドルウェアの追加
app.add_middleware(
    DBSessionMiddleware,
)

# リクエストミドルウェアの追加
app.add_middleware(
    RequestMiddleware,
)

# CORSミドルウェアの追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Environment.APP_FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーターの追加
app.include_router(
    api_router,
    prefix="/api",
)


@app.exception_handler(HTTPException)
async def disable_http_exception_handler(request, exc):
    raise exc


@app.get("/health-check")
def health_check():
    return "ok"
