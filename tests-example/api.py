from typing import Annotated

from fastapi import FastAPI
from fastapi import Path
from unit import Data

app = FastAPI()


@app.get("/api/v1/data/{n}")
def api_v1_get_data(
    *,
    n: Annotated[int, Path()],
) -> dict:
    dataobj = Data()
    return dataobj.get_data(n)


@app.get("/")
def handle_index() -> str:
    return "hello wrodlsadas"
