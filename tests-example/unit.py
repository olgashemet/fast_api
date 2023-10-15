from os import urandom

from devtools import debug


class Data:
    def get_data(self, num: int) -> dict:
        return {
            "a": self.get_dimension("a", num),
            "b": self.get_dimension("b", num),
        }

    def get_dimension(self, dim: str, num: int) -> str:
        return dim * num + urandom(8).hex()


if __name__ == "__main__":
    debug(Data().get_data(4))
