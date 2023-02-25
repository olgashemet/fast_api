from typing import Any


def send_message(m: Any) -> None:
    f = open("shared.txt", "w")
    f.write(m)
    f.flush()
    f.close()


def get_message() -> None:
    f = open("shared.txt", "r")
    f.seek(0)
    message = f.read()
    print(message)


def menu() -> None:
    while True:
        print("1 - rec, 2-send, ... - exit")
        choice = input("your choice: ")
        if choice == "1":
            print("get function")
            get_message()
            continue
        if choice == "2":
            m = input("message to send: ")
            send_message(m)
            continue
        break
