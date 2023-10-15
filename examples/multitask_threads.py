import time
from concurrent.futures.thread import ThreadPoolExecutor
from typing import Any

from devtools import debug


class CountHandler:
    def query_data(self) -> int:
        time.sleep(4)
        return 2579


class DataHandler:
    def query_data(self) -> list[dict[str, Any]]:
        time.sleep(8)
        return [{"sku": 2121}]


def main() -> None:
    with debug.timer("multitasking: threads") as timer:
        count_handler = CountHandler()
        data_handler = DataHandler()

        # todo: use max_workers <= CPU count * 2 + 1
        with ThreadPoolExecutor(max_workers=2) as executor:
            task_count = executor.submit(count_handler.query_data)
            task_data = executor.submit(data_handler.query_data)

            count = task_count.result()
            data = task_data.result()

        debug(count, data)

    timer.summary(verbose=True)


if __name__ == "__main__":
    main()
