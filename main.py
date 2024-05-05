from config import app
from handlers import finish_handler, catch_handler
from invokers import run_funnel
from database import create_database


async def main():
    await create_database()
    app.add_handler(finish_handler)
    app.add_handler(catch_handler)
    await app.start()
    await run_funnel()

app.run(main())