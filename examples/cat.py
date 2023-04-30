from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
conn = engine.connect()
metadata_obj = MetaData()
conn = engine.connect()

user = Table(
            "user",
            metadata_obj,
            Column("name", String(16), primary_key=True),
            Column("age", Integer),
        )
metadata_obj.create_all(engine)
class Cat:
    def __init__(self, name_1, age_1):
        self.name = name_1
        self.age=age_1
    def to_dict (self):
        return {"name": self.name, "age": self.age}

    def save(self):
        result = self.to_dict()
        conn.execute(user.insert(), result)

first_cast=Cat("Vasya", 10)
first_cast.save()
second_cast=Cat("Vova", 5)
second_cast.save()
third_cast=Cat("Murka", 1)
third_cast.save()

result_show = conn.execute(text("select  * from user"))
print(result_show.fetchall())