import time
from functools import wraps

import fastapi
from devtools import debug

app = fastapi.FastAPI()


def bench_sync(func):
    @wraps(func)
    def wrapper(*args, **kw):
        t0 = time.monotonic()
        try:
            return func(*args, **kw)
        finally:
            timing = time.monotonic() - t0
            debug(timing, func, args, kw)

    return wrapper


def bench_async(func):
    @wraps(func)
    async def wrapper(*args, **kw):
        t0 = time.monotonic()
        try:
            return await func(*args, **kw)
        finally:
            timing = time.monotonic() - t0
            debug(timing, func, args, kw)

    return wrapper


@app.get("/reports")
@bench_sync
def get_reports(
    n: int = fastapi.Query(),
):
    x = long_task(n)
    return x


@app.get("/healthcheck")
@bench_async
async def get_healthcheck():
    return "ok"
