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

        current = self._head
        if index == 0:
            current.value=obj
        else:
            for i in range(index):
                node_next=current.next
                if node_next is not None:
                    current=node_next
                else: return self._head
            current.value = obj


    def index(self, value: Any) -> int:
        current = self._head
        for i in range(value +1):
            if i == value:
                result = current.value
            else: current = current.next
            if not current:
                raise Exception('out of scope')
        return result






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
