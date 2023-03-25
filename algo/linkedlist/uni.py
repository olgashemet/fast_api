import dataclasses
from typing import Any, List
from typing import Optional
from typing import final


@final
@dataclasses.dataclass(slots=True)
class Node:
    value: Any
    next: Optional["Node"] = None  # noqa: A003,VNE003


class UniDirectionalLinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None
        self.__len = 0
        self.__last_node_changed = False
        self.__last_node: Node | None = None
        self.xxx = 0
        self.yyy = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if last_node := self._get_last_node():
            last_node.next = new_node
        else:
            self._head = new_node

        self.__len += 1
        self.__last_node = new_node
        self.__last_node_changed = False

    def insert(self, index: Any, obj: Any) -> None:  # noqa: CCR001
        """
        Inserts object before index
        """

        if not isinstance(index, int):
            err = f"{type(index)} object cannot be interpreted as an integer"
            raise TypeError(err)

        new_node = Node(obj)
        current = self._head

        if index == 0 or current is None or self.__len + index < 0:
            new_node.next = current
            self._head = new_node
        else:
            if index < 0:
                index = self.__len + index
            for _i in range(index - 1):
                if current.next is not None:
                    current = current.next
                else:
                    break
            new_node.next = current.next
            current.next = new_node

        self.__len += 1
        self.__last_node_changed = True

    def index(self, value: Any) -> Any:
        current = self._head
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                current = current.next
                index = index + 1

        raise ValueError(f"{value} is not in list")

    def _to_list(self) -> list:
        result = []

        current = self._head

        while current:
            result.append(current.value)
            current = current.next

        return result

    def _get_last_node(self) -> Node | None:
        if not self.__last_node_changed:
            return self.__last_node

        self.yyy += 1

        current = self._head
        while current:
            self.xxx += 1
            next_node = current.next
            if not next_node:
                break
            current = next_node

        self.__last_node = current
        self.__last_node_changed = False
        return current

    def __getitem__(self, index: Any) -> Any:  # noqa: CCR001
        if not isinstance(index, int):
            raise TypeError("list indices must be integers or slices")
        current = self._head
        if not current:
            raise ValueError("empty linked list")

        if self.__len + index < 0:
            raise IndexError("list index out of the range")

        if index < 0:
            index = self.__len + index
        for _i in range(index):
            if current.next:
                current = current.next
            else:
                raise IndexError("list index out of the range")
        return current.value

    def __setitem__(self, key: int, value: Any) -> None:  # noqa: CCR001
        if not isinstance(key, int):
            raise TypeError("not valid index")

        if self.__len + key < 0:
            raise IndexError("list index out of the range")

        current = self._head
        if current:
            if key <0:
                key = self.__len + key
            for _i in range(key):
                if current.next:
                    current = current.next
                else:
                    raise IndexError("list index out of the range")
            current.value = value

    def __delitem__(self, key: int) -> None:  # noqa: CCR001
        if not isinstance(key, int):
            raise TypeError("not valid index")

        current = self._head

        if self.__len + key < 0:
            raise IndexError("list assignment index out of range")

        if not current:
            raise ValueError("empty list")

        if key == 0 or self.__len + key == 0:
            self._head = self._head.next
            self.__len -= 1
            self.__last_node_changed = True

        if key < 0:
            key = self.__len + key

        for _i in range(key - 1):
            if current.next is not None:
                current = current.next
            else:
                raise IndexError("list index out of the range")
        if current.next:
            current.next = current.next.next
        self.__len -= 1
        self.__last_node_changed = True

    def __len__(self) -> int:
        return self.__len

    def __eq__(self, another: Any) -> bool:
        if self is another:
            return True
        if not isinstance(another, UniDirectionalLinkedList | list):
            return NotImplemented
        current = self._head
        current_1 = another._head
        while current:
            if not current_1:
                return False
            if current.value != current_1.value:
                return False
            else:
                current = current.next
                current_1 = current_1.next
        return True