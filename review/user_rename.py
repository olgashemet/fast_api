from typing import Annotated
from typing import Any

from devtools import debug
from pydantic import BaseModel
from pydantic import ValidationError
from pydantic import validator
from pydantic.fields import Field
from pydantic.types import StrictStr


class UserModel(BaseModel):
    name: Annotated[str, Field(min_length=1)]
    password: Annotated[StrictStr, Field()]
    age: Annotated[int, Field()]
    password2: Annotated[str, Field()] = "def pass 2"

    @validator("name")
    def check_lengh_name(
        cls: Any,  # noqa: N805
        name: str,
    ) -> None:
        if len(name) < 4:
            raise ValueError("name must be longer then 4 letters")


debug(
    UserModel(  # noqa: S106
        name="Ol888",
        password="1234",
        age="32",  # type: ignore
    )
)
try:
    UserModel(name="Ol888", password=123, age="32")  # type: ignore
except ValidationError as e:
    debug(e)
