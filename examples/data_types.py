from typing import Any
from typing import NamedTuple
from typing import Optional

from devtools import debug


class Data(NamedTuple):
    campaign_data: Any
    phone: str
    age: int
    xxx: Optional[int] = None


def useful_function() -> Data:
    campaign_data = "A"
    phone = "12"
    age = 12
    return Data(campaign_data, phone, age)


def get_division(arg1: str, arg2: str) -> float:
    debug(arg1, arg2)
    return 1.0


class get_overview_data:  # noqa: N801
    @property
    def ccpi(self) -> float:
        return get_division("fdsfs", "fdsfs") * 100

    @property
    def kpi(self) -> float:
        return 1 / 3 * self.ccpi


# ======================================


def existing_endpoint() -> None:
    value = useful_function()
    debug(value.phone)


def api_endpoint() -> None:
    resp1 = useful_function()
    debug(resp1.phone)

    resp2 = useful_function()
    debug(resp2.xxx)

    od = get_overview_data()
    debug(od.ccpi)
    debug(od.kpi)


if __name__ == "__main__":
    existing_endpoint()
    api_endpoint()
