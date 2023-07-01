from devtools import debug


class DTO:
    def __init__(self, **kw: dict) -> None:
        debug(DTO.__annotations__)
        debug(DTO.__init__.__annotations__)
        debug(self.__class__)
        debug(self.__class__.__annotations__)

        anno = self.__class__.__annotations__
        extra = kw.keys() - anno.keys()
        if extra:
            raise TypeError(f"unexpected params: {sorted(extra)}")

        for arg, value in kw.items():
            anno_type = anno[arg]
            if not isinstance(value, anno_type):
                raise TypeError(
                    f"arg `{arg=!r}` expected {anno_type}, got {type(value)}"
                )

            setattr(self, arg, value)


class User(DTO):
    name: str
    phone: str


a = User(name="n", phone="p", x=123)
debug(a.name, a.phone)
