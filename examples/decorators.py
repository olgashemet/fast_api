from typing import Any
from typing import Callable

from devtools import debug


class FastAPI2:
    def __init__(self) -> None:
        self._routes: dict[str, dict[str, Callable]] = {}

    def get(self, route: str) -> Callable:
        def decorator(handler: Callable) -> Callable:
            self._routes.setdefault(route, {})["GET"] = handler
            return handler

        return decorator

    def post(self, route: str) -> Callable:
        def decorator(handler: Callable) -> Callable:
            self._routes.setdefault(route, {})["POST"] = handler
            return handler

        return decorator


app: FastAPI2 = FastAPI2()


@app.get("/users/me")
def read_me() -> list[dict[str, Any]]:
    return [{"id": 1, "name": "me"}]


@app.get("/users")
def read_all_users() -> list[dict[str, Any]]:
    return [{"id": 1, "name": "me"}, {"id": 2, "name": "other"}]


@app.post("/users")
def create_user(**data: dict) -> dict:
    debug(data)
    return data


debug(app._routes)
