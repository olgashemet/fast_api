from typing import Annotated
from fastapi import FastAPI, Path
from unit import Data

app = FastAPI()


@app.get("/api/v1/data/{n}")
def api_v1_get_data(
    *,
    n: Annotated[int, Path()],
):
    dataobj = Data()
    return dataobj.get_data(n)


@app.get("/")
def api_v1_get_data():
    return "hello wrodlsadas"
