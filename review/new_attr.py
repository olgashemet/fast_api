from attrs import define
from attrs import field


@define
class C:
    _x: int = field(alias="_x")


c = C()
