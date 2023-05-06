from attrs import define, field
@define
class C:
    _x: int = field(alias="_x")

c = C()