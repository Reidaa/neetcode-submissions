class DynamicArray:
    
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._container = [None] * (self._capacity)
        print(f"Array {capacity} -> {self._container}")


    def get(self, i: int) -> int:
        if i + 1 > self._capacity:
            return None
        print(f"get {i} {self._container} -> {self._container[i]}")
        return self._container[i]


    def set(self, i: int, n: int) -> None:
        if self._container[i] == None:
            self._size += 1
        self._container[i] = n
        print(f"set {i} {n} -> {self._container}")


    def _getLastElementPos(self):
        last = None

        for i in range(1, len(self._container) + 1):
            v = self._container[i * -1]
            if v is not None:
                last = i * -1
                break

        print(f"_getLastElementPos -> {last}")
        return last


    def _getFirstEmptyPos(self):
        last = None

        for i in range(0, len(self._container)):
            v = self._container[i]
            if v is None:
                last = i
                break

        print(f"_getLastEmptyPos -> {last}")
        return last


    def pushback(self, n: int) -> None:
        print(f">>> pushback {n} {self._container}")
        
        if self.getSize() == self._capacity:
            self.resize()

        self._container[self._size] = n
        self._size += 1
        print(f"<<< pushback {n} -> {self._container}")
        

    def popback(self) -> int:
        print(f">>> popback {self._container}")
        self._size -= 1
        value = self._container[self._size]
        print(f"<<< popback {self._container} -> {value}")
        return value
 
    def resize(self) -> None:
        self._capacity *= 2

        new_container = [None] * self._capacity
        for i in range(0, len(self._container)):
            new_container[i] = self._container[i]
    
        self._container = new_container
        print(f"resize {self._container}")

    def getSize(self) -> int:
        print(f"getSize {self._container} -> {self._size}")
        return self._size
    
    def getCapacity(self) -> int:
        print(f"getCapacity {self._container} -> {self._capacity}")

        return self._capacity