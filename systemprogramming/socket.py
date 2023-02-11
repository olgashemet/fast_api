from typing import Any


def send_message(m: Any) -> None:  # noqa: VNE001
    f = open("shared.txt", "w")  # noqa: VNE001,SIM115
    f.write(m)
    f.flush()
    f.close()


def get_message() -> None:
    f = open("shared.txt", "r")  # noqa: SIM115,VNE001
    f.seek(0)
    message = f.read()
    print(message)  # noqa: T201


def menu() -> None:
    while True:
        print("1 - rec, 2-send, ... - exit")  # noqa: T201
        choice = input("your choice: ")
        if choice == "1":
            print("get function")  # noqa: T201
            get_message()
            continue
        if choice == "2":
            m = input("message to send: ")  # noqa: VNE001
            send_message(m)
            continue
        break
