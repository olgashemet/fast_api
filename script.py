import time
from functools import wraps
from typing import Any
from typing import Callable

import fastapi
from devtools import debug

app = fastapi.FastAPI()


def bench_sync(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kw: Any) -> Any:
        t0 = time.monotonic()
        try:
            return func(*args, **kw)
        finally:
            timing = time.monotonic() - t0
            debug(timing, func, args, kw)

    return wrapper


def bench_async(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args: Any, **kw: Any) -> Any:
        t0 = time.monotonic()
        try:
            return await func(*args, **kw)
        finally:
            timing = time.monotonic() - t0
            debug(timing, func, args, kw)

    return wrapper


def long_task(num: int) -> int:
    return num


@app.get("/reports")
@bench_sync
def get_reports(
    n: int = fastapi.Query(),  # noqa: B008,VNE001
) -> int:
    report = long_task(n)
    return report


@app.get("/healthcheck")
@bench_async
async def get_healthcheck() -> str:
    return "ok"
