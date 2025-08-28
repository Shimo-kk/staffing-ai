import os
from dotenv import load_dotenv
import pytest
import subprocess
from db.seeds.seed.seed_data import seed
from app.internal.share.config.database import (
    set_session,
    reset_session,
)
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def initialize_test_db():
    env = os.environ.copy()
    env["DATABASE_URL"] = env["DATABASE_URL_TEST"]
    subprocess.run(["alembic", "downgrade", "base"], check=True, env=env)
    subprocess.run(["alembic", "upgrade", "head"], check=True, env=env)
    seed(env["DATABASE_URL"])


@pytest_asyncio.fixture
async def db_session():
    db_url = os.environ["DATABASE_URL_TEST"]
    engine = create_async_engine(f"postgresql+asyncpg://{db_url}", echo=True)
    SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
    async with SessionLocal() as session:
        token = set_session(session)
        trans = await session.begin()
        try:
            yield session
            await trans.rollback()
        finally:
            reset_session(token)
            await session.close()
    await engine.dispose()
