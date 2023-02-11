import pytest

from algo.linkedlist.uni import UniDirectionalLinkedList


def test_uni_create() -> None:
    lst = UniDirectionalLinkedList()
    assert lst is not None


def test_uni_append() -> None:  # todo: split cases
    ul = UniDirectionalLinkedList()
    assert ul.to_list() == []

    ul.append(1)
    assert ul.to_list() == [1]

    ul.append("2")
    assert ul.to_list() == [1, "2"]

    ul.append([3])
    assert ul.to_list() == [1, "2", [3]]

    ul.insert(0, "olga")
    assert ul.to_list() == ["olga", "2", [3]]

    ul.insert(1, "mama")
    assert ul.to_list() == ["olga", "mama", [3]]

    ul.insert(6, "mama")
    assert ul.to_list() == ["olga", "mama", [3]]

    assert ul.index(0) == "olga"

    assert ul.index(2) == [3]

    # assert.unittest.Exception ('out of scope')
    # ul.index(10).Exception('out of scope')


def test_uni_empty_setitem() -> None:
    ll = UniDirectionalLinkedList()

    with pytest.raises(IndexError):
        ll.insert(0, "abc")  # todo: __setitem__


if __name__ == "__main__":
    test_uni_create()
