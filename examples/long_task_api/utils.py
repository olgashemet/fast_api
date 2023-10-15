import inspect
import time
from datetime import datetime
from functools import wraps
from typing import Callable
from typing import ParamSpec
from typing import TypeVar

from devtools import debug
from pydantic import BaseModel

P = ParamSpec("P")
T = TypeVar("T")


def debug_timing(func: Callable[P, T]) -> Callable[P, T]:
    """
    A decorator which prints decoratee's timings in stdout.
    """

    if inspect.iscoroutinefunction(func):

        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            t0 = time.monotonic()
            try:
                return await func(*args, **kwargs)
            finally:
                dt = time.monotonic() - t0
                timing = f"{dt:.2f} s"
                debug(timing, func, args, kwargs)

    else:

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            t0 = time.monotonic()
            try:
                return func(*args, **kwargs)
            finally:
                dt = time.monotonic() - t0
                timing = f"{dt:.2f} s"
                debug(timing, func, args, kwargs)

    wrapper = wraps(func)(wrapper)
    return wrapper


class Timing(BaseModel):
    begin: datetime
    end: datetime
    seconds: float


class JsonApiTimedPayloadMeta(BaseModel):
    timing: Timing


class JsonApiTimedPayload(BaseModel):
    data: T
    meta: JsonApiTimedPayloadMeta


def equip_response_with_timing(
    func: Callable[P, T]
) -> Callable[P, JsonApiTimedPayload]:
    if inspect.iscoroutinefunction(func):

        async def wrapper(
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> JsonApiTimedPayload:
            begin = datetime.utcnow()
            t0 = time.monotonic_ns()
            data = await func(*args, **kwargs)

            return JsonApiTimedPayload(
                data=data,
                meta=JsonApiTimedPayloadMeta(
                    timing=Timing(
                        begin=begin,
                        end=datetime.utcnow(),
                        seconds=(time.monotonic_ns() - t0) / 1e9,
                    ),
                ),
            )

    else:

        def wrapper(
            *args: P.args,
            **kwargs: P.kwargs,
        ) -> JsonApiTimedPayload:
            begin = datetime.utcnow()
            t0 = time.monotonic_ns()
            data = func(*args, **kwargs)

            return JsonApiTimedPayload(
                data=data,
                meta=JsonApiTimedPayloadMeta(
                    timing=Timing(
                        begin=begin,
                        end=datetime.utcnow(),
                        seconds=(time.monotonic_ns() - t0) / 1e9,
                    ),
                ),
            )

    wrapper = wraps(func)(wrapper)
    return wrapper
