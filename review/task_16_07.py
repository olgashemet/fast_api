"""
hex: 0123456789abcdef


7A1 =>

  7 * 16^2
+ A * 16^1
+ 1 * 16^0

1 16^1
2 1
"""

hex_values = "0123456789abcdef"


def xxx(hex_value: str) -> int:
    hex_value = hex_value.lower()
    return sum(
        hex_values.index(digit) * 16**pos
        for pos, digit in enumerate(hex_value[::-1])
    )


def xxx(input_value: str) -> int:  # type: ignore  # noqa: F811
    sum_result = 0
    for i in range(len(input_value), 0, -1):
        hex_digit = input_value[i - 1].lower()
        digit = hex_values.index(hex_digit)
        intt_sum = digit * 16 ** (len(input_value) - i)
        sum_result = sum_result + intt_sum
    return sum_result


assert xxx("bc") == int("bc", 16), xxx("bc")
raise SystemExit(0)

# tests

# interface = input("what interface you prefer? 1..4 : ")
# hex_value = "A0BCc"
# int_value = int(hex_value, 16)

# if interface == "1":
#     # option 1. simple function
#     err = f"{xxx(hex_value)!r} != {int_value!r}"
#     assert xxx(hex_value) == int_value, err

# elif interface == "2":
#     # option 2. class-service
#     xxx = XXX()  # noqa:T102,F821
#     assert xxx.convert(hex_value) == int_value

# elif interface == "3":
#     # option 3. class
#     xxx = XXX(hex_value)  # noqa: T102,F821
#     assert xxx.value == hex_value
#     assert xxx.to_int() == int_value

# elif interface == "4":
#     # option 4. class-usecase
#     xxx = XXX(hex_value)  # noqa: T102,F821
#     assert xxx.value == hex_value
#     assert xxx() == int_value

# else:
#     raise RuntimeError("please set interface: 1 .. 4")
