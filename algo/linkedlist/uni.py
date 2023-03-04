import dataclasses
from typing import Any
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

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if last_node := self._get_last_node():
            last_node.next = new_node
        else:
            self._head = new_node

    def insert(self, index: Any, obj: Any) -> None:  # noqa: CCR001
        new_node = Node(obj)
        current = self._head
        if isinstance(index, int) and (index >= 0):
            if index == 0 or current is None:
                new_node.next = self._head
                self._head = new_node
            else:
                for _i in range(index - 1):
                    if current.next is not None:
                        current = current.next
                    else:
                        break
                new_node.next = current.next
                current.next = new_node
        else:
            raise IndexError("not valid index")

    def index(self, value: Any) -> Any:
        current = self._head
        if not current:
            raise ValueError("empty list")
        index = 0
        while current:
            if current.value == value:
                return index
            else:
                current = current.next
                index = index + 1

        raise ValueError("no values available in the list")

    def to_list(self) -> list:
        result = []

        current = self._head

        while current:
            result.append(current.value)
            current = current.next

        return result

    def _get_last_node(self) -> Node | None:
        current = self._head

        while current:
            next_node = current.next
            if not next_node:
                return current
            current = next_node

        return current

    def __getitem__(self, index: Any) -> Any:
        if isinstance(index, int) and (index >= 0):
            current = self._head
            if current:
                for _i in range(index):
                    if current.next:
                        current = current.next
                    else:
                        raise IndexError("list index ou of the range")
                return current.value
            else:
                raise ValueError("empty linked list")
        else:
            raise TypeError("not valid index")

    def __setitem__(self, key: int, value: Any) -> None:
        if isinstance(key, int) and (key >= 0):
            current = self._head
            if current:
                for _i in range(key):
                    if current.next:
                        current = current.next
                    else:
                        raise IndexError("list index ou of the range")
                current.value = value
        else:
            raise TypeError("not valid index")

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int) or (key < 0):
            raise TypeError("not valid index")
        else:
            if key == 0 and self._head:
                self._head = self._head.next
            else:
                if self._head:
                    current = self._head
                    for _i in range(key - 1):
                        if current.next is not None:
                            current = current.next
                        else:
                            raise IndexError("list index ou of the range")
                    if current.next:
                        current.next = current.next.next
                else:
                    raise ValueError("empty list")

    def __len__(self) -> int:
        current = self._head
        length_list = 0
        while current:
            length_list = length_list + 1
            current = current.next
        return length_list
