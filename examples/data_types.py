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


# ======================================


def existing_endpoint():
    x = useful_function()
    debug(x.phone)


def api_endpoint():
    resp1 = useful_function()
    debug(resp1.phone)

    resp2 = useful_function()
    debug(resp2.xxx)


if __name__ == '__main__':
    existing_endpoint()
    api_endpoint()
