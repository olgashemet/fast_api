from typing import Callable

from devtools import debug


class FastAPI2:
    def __init__(self):
        self._routes: dict[str, dict[str, Callable]] = {}

    def get(self, route: str):
        def decorator(handler: Callable):
            self._routes.setdefault(route, {})["GET"] = handler
            return handler

        return decorator

    def post(self, route: str):
        def decorator(handler: Callable):
            self._routes.setdefault(route, {})["POST"] = handler
            return handler

        return decorator


app = FastAPI2()


@app.get("/users/me")
def read_me():
    return [{"id": 1, "name": "me"}]


@app.get("/users")
def read_all_users():
    return [{"id": 1, "name": "me"}, {"id": 2, "name": "other"}]


@app.post("/users")
def create_user(**data):
    debug(data)
    return data


debug(app._routes)
