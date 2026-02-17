import asyncio


LOGS = []


async def my_dependency():
    LOGS.append("start")
    yield "working"
    yield "test"
    LOGS.append("finish")

async def main():
    gen = my_dependency()
    async for value in gen:
        print(f"Получено значение {value}")


if __name__ == "__main__":
    asyncio.run(main())
    print(LOGS)
