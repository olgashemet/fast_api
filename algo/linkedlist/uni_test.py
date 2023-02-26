import pytest

from algo.linkedlist.uni import UniDirectionalLinkedList


def test_uni_create() -> None:
    lst = UniDirectionalLinkedList()
    assert lst is not None


def test_uni_append() -> None:
    ul = UniDirectionalLinkedList()
    assert ul.to_list() == []

    ul.append(1)
    assert ul.to_list() == [1]

    ul.append("2")
    assert ul.to_list() == [1, "2"]

    ul.append([3])
    assert ul.to_list() == [1, "2", [3]]


def test_insert_first() -> None:
    # insert as a first  node
    ul = UniDirectionalLinkedList()
    ul.insert(0, "123")
    assert ul.to_list() == ["123"]


def test_insert_beyond_limit() -> None:
    ul = UniDirectionalLinkedList()

    with pytest.raises(ValueError) as excinfo:
        ul.insert(100, "python100")
    assert str(excinfo.value) == "current is none"

    with pytest.raises(ValueError) as excinfo:
        ul.insert(2, "1")
    assert str(excinfo.value) == "current is none"


def test_insert_second() -> None:
    ul = UniDirectionalLinkedList()

    # insert as a second-last  node
    ul.append(1)
    ul.append(2)
    ul.insert(1, "olga")
    assert ul.to_list() == [1, "olga", 2]

    ul.append("123")

    ul.insert(1, "python")
    assert ul.to_list() == [1, "python", "olga", 2, "123"]

    with pytest.raises(ValueError) as excinfo:
        ul.insert(100, "end")
    assert str(excinfo.value) == "index beyond list"


def test_index() -> None:
    # test if value is  available in the list
    ul = UniDirectionalLinkedList()

    ul.append("123")
    assert ul.index("123") == 0

    # test if value is not available in the list
    with pytest.raises(ValueError):
        ul.index("1236")

    # test if value is  available in the list
    ul.append("1234")
    assert ul.index("1234") == 1


def test__getitem__() -> None:
    ul = UniDirectionalLinkedList()
    with pytest.raises(TypeError):
        ul.__getitem__(-1.5)

    ul.append("123")
    assert ul.__getitem__(0) == "123"

    ul.append("1234")
    assert ul.__getitem__(1) == "1234"

    with pytest.raises(IndexError):
        ul.__getitem__(2)


def test__setitem__() -> None:
    ul = UniDirectionalLinkedList()
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.__setitem__(1, "olga")
    assert ul.to_list() == [1, "olga", 3]

    with pytest.raises(TypeError):
        ul.__getitem__(-1.5)

    with pytest.raises(IndexError):
        ul.__setitem__(5, "new value")


def test__delitem__() -> None:
    ul = UniDirectionalLinkedList()
    ul.append(1)
    ul.append(2)
    ul.append(3)
    ul.append(4)

    ul.__delitem__(4)
    assert ul.to_list() == [1, 2, 3, 4]

    ul.__delitem__(3)
    assert ul.to_list() == [1, 2, 3]

    with pytest.raises(TypeError):
        ul.__delitem__(-5)

    with pytest.raises(IndexError):
        ul.__delitem__(20)

    ul.__delitem__(1)
    assert ul.to_list() == [1, 3]

    ul.__delitem__(0)
    assert ul.to_list() == [3]

    ul.__delitem__(0)
    assert ul.to_list() == []

    with pytest.raises(ValueError):
        ul.__delitem__(0)


if __name__ == "__main__":
    test_uni_create()
    test_uni_append()
    test_insert_first()
    test_insert_beyond_limit()
    test_insert_second()
    test_index()
    test__getitem__()
    test__setitem__()
    test__delitem__()
