class DynamicArray:
    
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._container = [None] * (self._capacity)


    def get(self, i: int) -> int:
        return self._container[i]


    def set(self, i: int, n: int) -> None:
        if self._container[i] == None:
            self._size += 1
        self._container[i] = n


    def pushback(self, n: int) -> None:
        
        if self.getSize() == self._capacity:
            self.resize()

        self._container[self._size] = n
        self._size += 1
        

    def popback(self) -> int:
        self._size -= 1
        value = self._container[self._size]
        return value
 
    def resize(self) -> None:
        self._capacity *= 2

        new_container = [None] * self._capacity
        for i in range(0, len(self._container)):
            new_container[i] = self._container[i]
    
        self._container = new_container

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity