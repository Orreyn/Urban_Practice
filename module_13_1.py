import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял шар номер {i}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    p1 = asyncio.create_task(start_strongman('Пол', 5))
    p2 = asyncio.create_task(start_strongman('Тони', 2))
    p3 = asyncio.create_task(start_strongman('Коул', 4))
    await p1
    await p2
    await p3

asyncio.run(start_tournament())