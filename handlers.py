import datetime

from pyrogram import filters, Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message

import database
import settings


async def create_new_user(tg_id: int):
    user = database.User()
    user.id = tg_id
    user.created_at = datetime.datetime.now()
    user.status = 'alive'
    user.stage = 0
    user.status_updated_at = datetime.datetime.now()
    return user


async def finish_by_trigger(client: Client, message: Message):
    tg_id: int = message.from_user.id

    user = await database.get_user(tg_id=tg_id)
    if user is None:
        user = await create_new_user(tg_id)

    user.status = 'finished'
    user.stage = 3
    user.status_updated_at = datetime.datetime.now()
    await database.add_user(user)


async def catch_new_user_and_pass_triggers(client, message: Message):
    """
    Добавляет юзеров в воронку, ловит триггер на отправку второго сообщения
    :param client:
    :param message:
    :return:
    """
    tg_id = message.from_user.id

    user = await database.get_user(tg_id=tg_id)
    if user is None:
        user = await create_new_user(tg_id)
        await database.add_user(user)

    if user.stage in settings.triggers_pass_stage.keys():
        for trigger in settings.triggers_pass_stage[user.stage]:
            if trigger in message.text:
                user.stage += 1
                user.status_updated_at = datetime.datetime.now()
        await database.add_user(user)

finish_handler = MessageHandler(finish_by_trigger, filters=(filters.regex(settings.trigger_finish[0]) |
                                                            filters.regex(settings.trigger_finish[1])))
catch_handler = MessageHandler(catch_new_user_and_pass_triggers, filters=(filters.text & filters.private))
