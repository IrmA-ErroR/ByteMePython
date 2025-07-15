import asyncio
import time

async def worker_task(name, delay):
    print(f"Задача {name}: начинаю, буду ждать {delay} сек.")
    await asyncio.sleep(delay)
    print(f"Задача {name}: завершена.")
    return f"Результат от {name}"

async def main_concurrent():
    start_time = time.time()
    print(f"Запуск конкурентных задач в {time.strftime('%X')}")

    # Создаем задачи для конкурентного выполнения
    task1 = asyncio.create_task(worker_task("A", 2))
    task2 = asyncio.create_task(worker_task("B", 1))
    task3 = asyncio.create_task(worker_task("C", 3))

    # Ожидаем завершения всех задач конкурентно
    # (Более удобный способ дождаться нескольких задач - asyncio.gather())
    results = await asyncio.gather(task1, task2, task3)

    print(f"\nВсе задачи завершены за {time.time() - start_time:.2f} сек.")
    print(f"Результаты: {results}")

if __name__ == "__main__":
    asyncio.run(main_concurrent())
