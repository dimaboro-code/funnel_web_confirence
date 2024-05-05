from __future__ import annotations

from datetime import datetime
from sqlalchemy import Integer, Text, DateTime, select, BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.exc import IntegrityError
from config import async_session, engine


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    """
    stage - текущая стадия обработки клиента.
    1 - начало воронки, 1 сообщение
    2 - продолжение, второе сообщение
    """
    __tablename__ = 'conf_users'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(Text, default='alive', nullable=False)
    status_updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    stage: Mapped[int] = mapped_column(Integer(), default=0, nullable=True)


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user: User):
    async with async_session() as session:
        session.add(user)
        try:
            await session.commit()
            await session.close()
            print('Статус юзера обновлен')
        except IntegrityError:
            print('Ошибка при создании или изменении данных пользователя:', user.id)
    return user


async def get_user(tg_id: int):
    async with async_session() as session:
        return await session.get(User, tg_id)


async def delete_user():
    pass


async def get_all_users(status: str | None = None):
    async with async_session() as session:
        async with session.begin():
            if status:
                query = await session.execute(select(User).filter(User.status == status))
            else:
                query = await session.execute(select(User))
            return query.scalars().all()
