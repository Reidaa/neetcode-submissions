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
        print(f">>> get {index} {self.getValues()}")
        if index >= self._size:
            return -1

        if self._head is None:
            return -1

        curr = self._head

        for i in range(0, index):
            curr = curr.next

        print(f">>> get {index} {self.getValues()} -> {curr.value}")
        return curr.value


    def insertHead(self, val: int) -> None:
        new_node = Node(val, None)
        
        if self._head is None or self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        
        self._size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val, None)

        if self._head is None or self._tail is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1


    def remove(self, index: int) -> bool:
        if index >= self._size:
            return False

        if self._head is None:
            return False

        if self._size == 1:
            self._head = None
            self._tail = None
            self._size -= 1
            return True

        if index == 0:
            self._head = self._head.next
            self._size -= 1
            return True 
        
        curr = self._head
        for i in range(0, index-1):
            curr = curr.next
        prev_node = curr
            
        if index == self._size - 1:
            prev_node.next = None
            self._tail = prev_node
        else:
            prev_node.next = prev_node.next.next
        
        self._size -= 1
        return True


    def getValues(self) -> List[int]:
        l = []
        now = self._head

        if now is None:
            return []

        for i in range(0, self._size ):
            if now is None:
                break
            l.append(now.value)
            now = now.next

        return l
        
