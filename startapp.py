import asyncio

async def run_parser():
    print("Запуск парсера...")
    process = await asyncio.create_subprocess_exec('python', 'pars.py')
    await process.wait()
    print("Парсер закінчив роботу.")

async def run_bot():
    print("Запуск Telegram бота...")
    process = await asyncio.create_subprocess_exec('python', 'bot.py')
    await process.wait()
    print("Telegram бот завершив роботу.")

async def main():
    task1 = asyncio.create_task(run_parser())
    task2 = asyncio.create_task(run_bot())
    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())
