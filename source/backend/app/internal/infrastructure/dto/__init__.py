from datetime import datetime
from uuid import UUID
from uuid6 import uuid7
from sqlalchemy.dialects.postgresql import UUID as PgUUID
from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class BaseDTO(Base):
    """
    DTOクラスのベース
    """

    __abstract__ = True

    id: Mapped[UUID] = mapped_column(
        PgUUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid7,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )

    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )


class MasterDTO(Base):
    """
    DTOクラスのベース
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
