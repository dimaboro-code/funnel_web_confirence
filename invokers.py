import asyncio
import datetime

from pyrogram import errors
import settings
from config import app
from database import get_all_users, add_user


async def go_funnel():
    """
    как это работает
    получаем всех юзеров из бд
    для каждого сравниваем разницу между временем обновления и текущим и требуемую разницу во времени
    если текущая разница больше или равна нужной - отправляем сообщение.
    Если сообщение не отправилось, то оно обрабатывается как исключение и пользователь меняет статус на мертвого
    messages_to_send - список из пар текст - время (разница времени) типа кортеж.
    Соответственно, по индексу 0 мы получаем первый элемент (сообщение), по индексу 1 второй (дэльту времени)
    :return:
    """
    users = await get_all_users(status='alive')
    for user in users:
        print(settings.messages_to_send[user.stage][1])
        if datetime.datetime.now() - user.status_updated_at >= settings.messages_to_send[user.stage][1]:
            try:
                await app.send_message(user.id, settings.messages_to_send[user.stage][0])
                user.stage += 1
                user.status_updated_at = datetime.datetime.now()
                if user.stage == 3:
                    user.status = 'finished'
            except errors.UserDeactivated or errors.UserBlocked:
                user.status = 'dead'
            except Exception as e:
                print('непредвиденная ошибка:', e)
                user.status = 'dead'
            await add_user(user)


async def run_funnel():
    """
    бесконечный цикл, согласно условию в тз
    :return:
    """
    while True:
        await go_funnel()
        await asyncio.sleep(1)
