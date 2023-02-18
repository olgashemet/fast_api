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
    try:
        ul.insert(100, "python100")
    except ValueError:
        "index beyond list"
        pass

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

def test_index() -> None:

# test if value is  available in the list
    ul = UniDirectionalLinkedList()

    ul.append("123")
    prime_numbers = [2, 3, 5, 7]
    assert ul.index("123") == 0

# test if value is not available in the list
    try:
        ul.index("1236")
    except ValueError:
        "no values available in the list"
        pass

# test if value is  available in the list
    ul.append("1234")
    assert ul.index("1234") == 1


if __name__ == "__main__":
    test_uni_create()
    test_uni_append()
    test_insert_first()
    test_insert_beyond_limit()
    test_insert_second()
    test_index()

