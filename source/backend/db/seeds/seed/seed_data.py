from typing import Type, TypeVar
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from app.internal.share.constant.constant import Constants

T = TypeVar("T")


def seed(url: str) -> None:
    engine = create_engine(f"postgresql+psycopg2://{url}")
    session_local: sessionmaker = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    session = session_local()

    try:

        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def _seed(session: Session, cls: Type[T], data_list: list[T]):
    print("Seed:" + str(cls))

    # 既存のデータを取得
    existing_data = session.query(cls).all()
    # id属性が存在するかを確認しながら辞書を作成
    existing_data_dict = {}
    for record in existing_data:
        if hasattr(record, "id"):
            existing_data_dict[getattr(record, "id")] = record

    data_list_dict = {}
    for record in data_list:
        if hasattr(record, "id"):
            data_list_dict[getattr(record, "id")] = record

    # 挿入またはスキップするレコードを処理
    for record in data_list:
        record_id = getattr(record, "id", None)
        if record_id is not None and record_id in existing_data_dict:
            existing_record = existing_data_dict[record_id]
            # 既存のレコードと内容が同じ場合はスキップ
            if all(
                getattr(existing_record, attr, None) == getattr(record, attr, None)
                for attr in vars(record)
                if not attr.startswith("_")
            ):
                continue
            # 既存のレコードと内容が異なる場合はスキップ
            else:
                continue
        else:
            # 新しいレコードを追加
            session.add(record)

    # data_listに存在しない既存レコードを削除
    for record in existing_data:
        record_id = getattr(record, "id", None)
        if record_id is not None and record_id not in data_list_dict:
            session.delete(record)
