import asyncio

from devtools import debug


class CountHandler:
    async def query_data(self):
        await asyncio.sleep(4)
        return 2579


class DataHandler:
    async def query_data(self):
        await asyncio.sleep(8)
        return [{"sku": 2121}]


async def main():
    with debug.timer("multitasking: asyncio") as timer:
        count_handler = CountHandler()
        data_handler = DataHandler()

        # todo: use asyncio.TaskGroup on Python >= 3.11
        task_count = asyncio.create_task(
            count_handler.query_data(),
            name="count",
        )
        task_data = asyncio.create_task(
            data_handler.query_data(),
            name="data",
        )

        count, data = await asyncio.gather(task_count, task_data)

        debug(count, data)

    timer.summary(verbose=True)


if __name__ == "__main__":
    asyncio.run(main())
