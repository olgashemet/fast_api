from algo.linkedlist.uni import UniDirectionalLinkedList
from typing import Any
import pytest


@pytest.fixture(params=[list, UniDirectionalLinkedList])
def common_arg1(request) -> Any:
    return request.param


def test_uni_create(common_arg1: Any) -> None:
    lst = common_arg1()
    assert lst is not None


def test_uni_append(common_arg1: Any) -> None:
    ul = common_arg1()
    assert ul == []

    ul.append(1)
    assert ul == [1]

    ul.append("2")
    assert ul == [1, "2"]

    ul.append([3])
    assert ul == [1, "2", [3]]

    ul.append(None)
    assert ul == [1, "2", [3], None]

    ul.append(NotImplemented)
    assert ul == [1, "2", [3], None, NotImplemented]


def test_insert_first(common_arg1: Any) -> None:
    # insert as a first  node
    li = common_arg1()

    li.insert(0, "123")
    assert li == ["123"]

    li.insert(0, "456")
    assert li == ["456", "123"]

    li.insert(-1, "-1")
    assert li == ["456", "-1", "123"]


def test_insert_beyond_limit(common_arg1: Any) -> None:
    ul = common_arg1()
    ul.insert(1000, "test")
    assert ul == ["test"]

    ul.insert(0, "0_test")
    assert ul == ["0_test", "test"]

    ul.insert(1, "1234")
    assert ul == ["0_test", "1234", "test"]

    ul.insert(1000000, "1000000")
    assert ul == ["0_test", "1234", "test", "1000000"]

    ul.insert(-1, "python100")
    assert ul == ["0_test", "1234", "test", "python100", "1000000"]

    ul.insert(-1000, "python100")
    assert ul == ["python100", "0_test", "1234", "test", "python100", "1000000"]

    with pytest.raises(TypeError) as excinfo:
        ul.insert(1.5, "python100")
    assert "object cannot be interpreted as an integer" in str(excinfo.value)


def test_index(common_arg1: Any) -> None:
    # test if value is  available in the list
    ul = common_arg1()

    ul.append("123")
    assert ul.index("123") == 0

    # test if value is not available in the list
    with pytest.raises(ValueError) as excinfo:
        ul.index("1236")
    assert "is not in list" in str(excinfo.value)

    # test if value is  available in the list
    ul.append("1234")
    assert ul.index("1234") == 1


def test__getitem__(common_arg1: Any) -> None:
    ul = common_arg1()
    with pytest.raises(TypeError) as excinfo:
        ul[-1.5]
        assert "list indices must be integers or slices, not float" in str(excinfo.value)

    ul.append("123")
    assert ul[0] == "123"

    assert ul[-1] == "123"

    with pytest.raises(IndexError) as excinfo:
        ul[-10]
        assert "list index out of range" in str(excinfo.value)

    ul.append("1234")
    assert ul[1] == "1234"
    assert ul[-2] == "123"


def test__setitem__(common_arg1: Any) -> None:
    ul = common_arg1()
    ul.append(1)
    ul.append(2)
    ul.append(3)

    ul[1] = "olga"
    assert ul == [1, "olga", 3]

    ul[-1] = 4
    assert ul == [1, "olga", 4]

    ul[0] = 4
    assert ul == [4, "olga", 4]

    ul[-3] = 6
    assert ul == [6, 'olga', 4]

    with pytest.raises(TypeError) as excinfo:
        ul[-1.5]
        assert "not valid index" in str(excinfo.value)

    with pytest.raises(IndexError) as excinfo:
        ul[10] = "new value"
        assert "list assignment index out of range" in str(excinfo.value)

    with pytest.raises(IndexError) as excinfo:
        ul[-10] = "new value"
        assert "list assignment index out of range" in str(excinfo.value)


def test__delitem__(common_arg1: Any) -> None:
    ul = common_arg1()
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.append(4)
    ul.append(5)

    del ul[4]
    assert ul == [1, 2, 3, 4]

    del ul[3]
    assert ul == [1, 2, 3]

    del ul[1]
    assert ul == [1, 3]

    del ul[-1]
    assert ul == [1]

    with pytest.raises(IndexError) as excinfo:
        del ul[-20]
    assert "list assignment index out of range" in str(excinfo.value)

    del ul[-1]
    assert ul == []

    with pytest.raises(IndexError) as excinfo:
        del ul[-20]
    assert "list assignment index out of range" in str(excinfo.value)


def test__len__(common_arg1: Any) -> None:
    ul = common_arg1()
    assert len(ul) == 0

    ul.append(1)
    assert len(ul) == 1


def test__equal__(common_arg1: Any) -> None:
    li = common_arg1()

    assert [] == li
    assert li == []
    assert li == li


if __name__ == "__main__":
    test_uni_create()
    test_uni_append()
    test_insert_first()
    test_insert_beyond_limit()
    test_index()
    test__getitem__()
    test__setitem__()
    test__delitem__()
    test__len__()
