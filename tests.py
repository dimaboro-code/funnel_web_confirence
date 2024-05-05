import asyncio
import datetime

from database import add_user, User, create_database, get_all_users

mock = User(
    id=1234567890333,
    created_at=datetime.datetime.now(),
    status='alive',
    status_updated_at=datetime.datetime.now(),
    stage=0
)
async def test_db():
    await create_database()
    user = await add_user(mock)
    print('add user:', user)
    users = await get_all_users(status='alive')
    print('all users:', users)


asyncio.run(test_db())