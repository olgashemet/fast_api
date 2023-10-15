import fastapi

from .utils import equip_response_with_timing

api = fastapi.FastAPI()


@api.get("/healthz")
@equip_response_with_timing
async def handle_get_healthz():
    return "health ok"


@api.get("/reports/async/cpu")
@equip_response_with_timing
async def handle_reports_async_cpu():
    pass


@api.get("/reports/async/io")
@equip_response_with_timing
async def handle_reports_async_io():
    pass


@api.get("/reports/sync/cpu")
@equip_response_with_timing
def handle_reports_sync_cpu():
    pass


@api.get("/reports/sync/io")
@equip_response_with_timing
def handle_reports_sync_io():
    pass
