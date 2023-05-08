from devtools import debug
from typing import NamedTuple, Any, Optional


class Data(NamedTuple):
    campaign_data: Any
    phone: str
    age: int
    xxx: Optional[int] = None


def useful_function() -> Data:
    campaign_data="A"
    phone="12"
    age=12
    return Data(campaign_data, phone, age)


class get_overview_data:
    @property
    def ccpi(self) -> float:
        return get_division("fdsfs", "fdsfs") * 100

    @property
    def kpi(self) -> float:
        return 1 / 3 * self.ccpi

# ======================================


def existing_endpoint():
    x = useful_function()
    debug(x.phone)


def api_endpoint():
    resp1 = useful_function()
    debug(resp1.phone)

    resp2 = useful_function()
    debug(resp2.xxx)

    od = get_overview_data()
    debug(od.ccpi)
    debug(od.kpi)


if __name__ == '__main__':
    existing_endpoint()
    api_endpoint()
