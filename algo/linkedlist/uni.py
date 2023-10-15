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

        if index == 0 or current is None or len(self) + index < 0:
            new_node.next = current
            self._head = new_node
        elif len(self) + index > 0:
            if index < 0:
                index = len(self) + index
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
        if isinstance(index, int):
            current = self._head
            if current:
                if index < 0:
                    index = self.__len__() + index
                if index < 0:
                    raise IndexError("list index out of the range")
                for _i in range(index):
                    if current.next:
                        current = current.next
                    else:
                        raise IndexError("list index out of the range")
                return current.value
            else:
                raise ValueError("empty linked list")
        else:
            raise TypeError("list indices must be integers or slices")

    def __setitem__(self, key: int, value: Any) -> None:  # noqa: CCR001
        if isinstance(key, int) and (key >= 0 or self.__len__() + key >= 0):
            current = self._head
            if current:
                if key < 0:
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

        if (key == 0 or self.__len__() + key == 0) and self._head:
            self._head = self._head.next
            self.__len -= 1
            self.__last_node_changed = True
        elif self._head and len(self) + key > 0:
            if key < 0:
                key = len(self) + key
            if self._head:
                current = self._head
                for _i in range(key - 1):
                    if current.next is not None:
                        current = current.next
                    else:
                        raise IndexError("list index out of the range")
                if current.next:
                    current.next = current.next.next
                self.__len -= 1
                self.__last_node_changed = True
            else:
                raise ValueError("empty list")
        else:
            raise IndexError("list assignment index out of range")

    def __len__(self) -> int:
        return self.__len

    def __eq__(self, another: Any) -> bool:
        if self is another:
            return True
        if not isinstance(another, UniDirectionalLinkedList | list):
            return NotImplemented
        return self._to_list() == another

    def split_linked_list(self) -> tuple:
        current = self._head
        list_1 = []
        list_2 = []
        if not current:
            raise ValueError("empty list")
        else:
            while current:
                if current.value % 2 == 0:
                    list_1.append(current.value)
                else:
                    list_2.append(current.value)
                current = current.next
        return (list_1, list_2)

    def split_linked_list_into_linked_list(self) -> None:
        current = self._head
        even_start = None
        even_end = None
        if not current:
            raise ValueError("empty list")
        else:
            while current:
                if current.value % 2 == 0:
                    if even_start is None:
                        even_start = current
                        even_end = even_start
                    else:
                        assert even_end is not None
                        even_end.next = current
                        # delem odin sdvig v pravo
                        even_end = even_end.next

                current = current.next

                #     next_node = Node(current.value)
                #     current_node.next = next_node
                #     current_node=current_node.next
                # current = current.next
        # return current_odd

        # self._head = new_node
        # new_node = Node(value)
        # if last_node := self._get_last_node():
        #     last_node.next = new_node
        # else:
        #     self._head = new_node
        # current = self._head
        # while current:
        #     self.xxx += 1
        #     next_node = current.next
        #     if not next_node:
        #         break
        #     current = next_node

        # new_node = Node(obj)
        # current = self._head
        #
        # if index == 0 or current is None or len(self) + index < 0:
        #     new_node.next = current
