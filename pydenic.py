from pydantic import BaseModel, ValidationError, validator
from pydantic.fields import Field
from pydantic.types import StrictStr


class UserModel(BaseModel):
    name: str = Field(..., min_length=1)
    password: StrictStr
    age: int = 30
    password2='atr'


    @validator('name')
    def check_lengh_name(cls, name):
        if len(name) < 4:
            raise ValueError('name must be longer then 4 letters')

print(UserModel(name='Ol888', password=1234, age='32'))
try:
    UserModel(name='Ol888', password=123, age='32')
except ValidationError as e:
    print(e)




