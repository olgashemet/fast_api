from io import StringIO
from itertools import count
from pathlib import Path
from typing import IO

CHUNK_SIZE = 11  # todo : tune it


def read_chunks(stream: IO) -> None:
    stream.seek(0)

    for i in count(1):
        lines = (stream.readline() for _ in range(CHUNK_SIZE))
        lines_stripped = (line.strip() for line in lines)
        lines_nonempty = [line for line in lines_stripped if line]

        if not lines_nonempty:
            break

        buffer = StringIO()
        buffer.writelines(lines_nonempty)
        buffer.seek(0)
        print(f"copy to db: {i=}, {len(lines_nonempty)=}")


def write_initial(stream: IO, sz: int = 100) -> None:
    for i in range(sz):
        stream.write(f"{i}\n")


def bench():
    # todo: physical file
    # todo: use StringIO when size(path) <= 0.1 * psutil.virtual_memory().available
    # todo: physical file size: path.stat().st_size
    path = Path("./xxx.txt")

    with path.open("w") as stream:
        write_initial(stream)

    with path.open("r") as stream:
        read_chunks(stream)


if __name__ == "__main__":
    bench()
