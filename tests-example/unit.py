from devtools import debug
from os import urandom


class Data:
    def get_data(self, n):
        return {
            "a": self.get_dimension("a", n),
            "b": self.get_dimension("b", n),
        }

    def get_dimension(self, dim, n):
        return dim * n + urandom(8).hex()


if __name__ == "__main__":
    debug(Data().get_data(4))
