import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

'''Вывод:
Task A: Compute factorial(2)...
Task B: Compute factorial(2)...
Task C: Compute factorial(2)...
(тк процессы начались одновременно и прошло меньше 1 секунды)
Task A: factorial(2) = 2
Task B: Compute factorial(3)...
Task C: Compute factorial(3)...
(первая программа завершилась - остальные отправились считать факториал 3х)
Task B: factorial(3) = 6
Task C: Compute factorial(4)...
(вторая дошла до ответа - у последней ещё факториал 4х)
Task C: factorial(4) = 24
(программа закончилась, когда закончились все циклы)'''