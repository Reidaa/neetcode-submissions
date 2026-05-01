class Node:
    __slots__ = ("value", "next")
    
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None = None):
        self.value = value
        self.next = next

class LinkedList:

    
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    
    def get(self, index: int) -> int:
        if index >= self._size:
            return -1

        now = self._head
        if not now:
            return -1

        for i in range(0, index):
            now = now.next

        return now.value


    def insertHead(self, val: int) -> None:
        new_node = Node(val, None)
        
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        
        self._size += 1

    def insertTail(self, val: int) -> None:
        self._size += 1
        new_node = Node(val, None)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node


    def remove(self, index: int) -> bool:
        if index >= self._size:
            return False
        self._size -= 1

        if self._size == 0:
            self._head = None
            self._tail = None
            return True

        if index == 0:
            self._head = self._head.next
            return True 
        
        now = self._head
        for i in range(0, index-1):
            now = now.next
        prev_node = now
        to_remove = now.next
            
        if self._size == index:
            prev_node.next = None
            self._tail = prev_node
        else:
            prev_node.next = to_remove.next
        return True


    def getValues(self) -> List[int]:
        l = []
        i = 0
        now = self._head

        if not now:
            return []

        for i in range(0, self._size ):
            if now is None:
                break
            l.append(now.value)
            now = now.next

        return l
        
