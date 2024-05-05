"""
В данном файле собраны все элементы настроек непосредственно бота - текст сообщений, время отправки
и прочее
"""
import datetime

messages_to_send = [
    ('Текст1', datetime.timedelta(minutes=6)),
    ('Текст2', datetime.timedelta(minutes=49)),
    ('Текст3', datetime.timedelta(days=1, hours=2))
]

triggers_pass_stage = {1: ['Триггер1']}  # пропуск второй стадии - триггер «триггер1». вторая по нумерации - 1


trigger_finish = ['прекрасно', 'ожидать']
