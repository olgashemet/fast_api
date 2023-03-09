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
        """
        Inserts object before index
        """

        new_node = Node(obj)
        current = self._head
        if isinstance(index, int):
            if index == 0 or current is None or self.__len__() + index < 0:
                new_node.next = current
                self._head = new_node
            elif self.__len__() + index > 0:
                if index >= 0:
                    index = index
                else:
                    index = self.__len__() + index
                for _i in range(index - 1):
                    if current.next is not None:
                        current = current.next
                    else:
                        break
                new_node.next = current.next
                current.next = new_node
        else:
            raise TypeError(f"{type(index)} object cannot be interpreted as an integer")

    def index(self, value: Any) -> Any:  # noqa: CCR001
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
        current = self._head

        while current:
            next_node = current.next
            if not next_node:
                return current
            current = next_node

        return current

    def __getitem__(self, index: Any) -> Any:  # noqa: CCR001
        if isinstance(index, int):
            current = self._head
            if current:
                if index >= 0:
                    index = index
                else:
                    index = self.__len__() + index
                    if index < 0:
                        raise IndexError("list index ou of the range")
                for _i in range(index):
                    if current.next:
                        current = current.next
                    else:
                        raise IndexError("list index ou of the range")
                return current.value
            else:
                raise ValueError("empty linked list")
        else:
            raise TypeError("list indices must be integers or slices, not float")

    def __setitem__(self, key: int, value: Any) -> None:  # noqa: CCR001
        if isinstance(key, int) and (key >= 0 or self.__len__() + key >= 0):
            current = self._head
            if current:
                if key >= 0:
                    key = key
                else:
                    key = self.__len__() + key
                for _i in range(key):
                    if current.next:
                        current = current.next
                    else:
                        raise IndexError("list index out of the range")
                current.value = value
        elif self.__len__() + key < 0:
            raise IndexError("list index out of the range")
        else:
            raise TypeError("not valid index")

    def __delitem__(self, key: int) -> None:  # noqa: CCR001
        if not isinstance(key, int):
            raise TypeError("not valid index")
        else:
            if (key == 0 or self.__len__() + key == 0) and self._head:
                self._head = self._head.next
            elif self._head and self.__len__() + key > 0:
                if key > 0:
                    key = key
                else:
                    key = self.__len__() + key
                if self._head:
                    current = self._head
                    for _i in range(key - 1):
                        if current.next is not None:
                            current = current.next
                        else:
                            raise IndexError("list index out of the range")
                    if current.next:
                        current.next = current.next.next
                else:
                    raise ValueError("empty list")
            else:
                raise IndexError("list assignment index out of range")

    def __len__(self) -> int:
        current = self._head
        length_list = 0
        while current:
            length_list = length_list + 1
            current = current.next
        return length_list

    def __eq__(self, another: Any) -> bool:
        if not isinstance(another, UniDirectionalLinkedList | list):
            return NotImplemented
        return self._to_list() == another
