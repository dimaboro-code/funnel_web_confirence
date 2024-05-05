import os
from pyrogram import Client
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker


env = load_dotenv()
if not env:
    print('.env файл не найден')


api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
DATABASE_URL = os.getenv('DATABASE_URL')

app = Client(name='userbot', api_id=api_id, api_hash=api_hash)

engine: AsyncEngine = create_async_engine(
    DATABASE_URL, echo=False, connect_args={"ssl": 'prefer'}
)
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)
