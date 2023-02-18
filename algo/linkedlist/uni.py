import dataclasses
from typing import Any
from typing import Optional
from typing import final


@final
@dataclasses.dataclass(slots=True)
class Node:
    value: Any
    next: Optional["Node"] = None


class UniDirectionalLinkedList:
    def __init__(self) -> None:
        self._head: Node | None = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if last_node := self._get_last_node():
            last_node.next = new_node
        else:
            self._head = new_node

    def insert(self, index: int, obj: Any) -> None:
        new_node = Node(obj)
        current = self._head
        if index == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            for i in range(index - 1):
                if current:
                    node_next = current.next
                    if node_next is not None:
                        current = node_next
                    else:
                        raise ValueError("index beyond list")
                else:
                    raise ValueError("current is none")
            if current:
                new_node.next = current.next
                current.next = new_node

    def index(self, value: Any) -> int:
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
            next = current.next
            if not next:
                return current
            current = next

        return current
