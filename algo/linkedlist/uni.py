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

    # todo: __getitem__
    # todo: __setitem__
    # todo: __delitem__
    def insert(
        self, index: int, obj: Any
    ) -> Any:  # fixme: rename to __setitem__
        # todo: if index out of range: raise IndexError
        current = self._head
        if index == 0:
            current.value = obj  # type: ignore
        else:
            for _i in range(index):
                node_next = current.next  # type: ignore
                if node_next is not None:
                    current = node_next
                else:
                    return self._head
            current.value = obj  # type: ignore

    def index(self, value: Any) -> Any:
        current = self._head
        for i in range(value + 1):
            if i == value:
                result = current.value  # type: ignore
            else:
                current = current.next  # type: ignore
            if not current:
                raise Exception("out of scope")  # todo: ValueError
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
            next = current.next  # noqa: A001,VNE003
            if not next:
                return current
            current = next

        return current
