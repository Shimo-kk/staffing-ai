import sys
from contextvars import ContextVar, Token
from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.internal.share.environment.environment import Environment

if "pytest" in sys.modules:
    url = f"postgresql+asyncpg://{Environment.DATABASE_URL_TEST}"
else:
    url = f"postgresql+asyncpg://{Environment.DATABASE_URL}"

engine = create_async_engine(url, echo=False)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

_session_ctx: ContextVar[Optional[AsyncSession]] = ContextVar(
    "_session_ctx", default=None
)


def set_session(session: AsyncSession) -> Token[AsyncSession | None]:
    return _session_ctx.set(session)


def get_session() -> Optional[AsyncSession]:
    return _session_ctx.get()


def reset_session(token: Token[AsyncSession | None]):
    _session_ctx.reset(token)
