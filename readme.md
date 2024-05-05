# Funnel Web Conference
## Описание проекта
Проект создан в качестве тестового задания для отклика на вакансию Миннегалиева Салиха Фаридовича 
Программист-разработчик Python.
Задача - создать инструмент для автоматического ведения пользователей по воронке продаж, автоматической рассылки 
сообщений по установленным правилам, а такде непрерывного мониторинга состояния лидов и их учета.
## Использованные технологии
- Python 3.12
- Pyrogram 2.0.106
- SQLAlchemy 2.0.29
- Postgres

## Использование скрипта
1. Заменить файл .env-example на .env, по образцу вставить в него нужные значения. Для упрощения работы я использую 
2. полную ссылку на базу данных вместо предоставляемого ORM конструктора.
2. Запустить консоль пайтон, перейти в папку со скриптом
3. Установить нужные зависимости. Это можно сделать командой 
``` pip install -r requirements.txt ```
4. запустить скрипт командой ```python main.py```
5. Выполнить инструкции от Pyrogram

## Изменение настроек скрипта
> Скрипт создан, чтобы отправлять определенные сообщения по определенному таймингу.

Чтобы добавить новые сообщения, новые тайминги, новые условия для скипов требуется открыть файл settings.py и внести 
соответствующие изменения.

## Лицензия
Данный код создан в демонстрационных целях, может использоваться кем угодно по своему усмотрению. 

С уважением, Dimaboro.