from abc import ABC, abstractmethod
import numpy as np

class ADTList(ABC):
    DEFAULT_SIZE: int = 10
    @abstractmethod
    def size(self) -> int: ...
    @abstractmethod
    def is_empty(self) -> bool: ...
    @abstractmethod
    def is_full(self) -> bool: ...
    @abstractmethod
    def insert(self, element: object, pos: int) -> None: ...
    @abstractmethod
    def insert_first(self, element: object) -> None: ...
    @abstractmethod
    def insert_last(self, element: object) -> None: ...
    @abstractmethod
    def remove(self, pos: int) -> object: ...
    @abstractmethod
    def remove_first(self) -> object: ...
    @abstractmethod
    def remove_last(self) -> object: ...
    @abstractmethod
    def get(self, pos: int) -> object: ...
    @abstractmethod
    def search(self, element: object) -> int: ...

class ArrayList(ADTList):
    def __init__(self, size: int = ADTList.DEFAULT_SIZE) -> None:
        self._elements = np.empty(size, object)
        self._count: int = 0

    def __len__(self) -> int:
        return self._count
    
    def __str__(self) -> str:
        return "[" + " ".join([str(elm) for elm in self]) + "]"
    
    def __iter__(self) -> object:
        for elm in self._elements[:self._count]:
            yield elm

    def __ensure_capacity(self) -> None:
        if len(self) == len(self._elements):
            self._elements = np.concatenate((self._elements,
            np.empty(len(self._elements), object)))

    def size(self) -> int:
        return len(self)
    
    def is_empty(self) -> bool:
        return self._count == 0
    
    def is_full(self) -> bool:
        return False
    
    def insert(self, element: object, pos: int) -> None:
        if (pos < 0 or pos > self._count):
            raise IndexError()
        self.__ensure_capacity()
        for i in range(self._count - 1, pos - 1, -1):
            self._elements[i + 1] = self._elements[i]
        self._elements[pos] = element
        self._count += 1

    def insert_first(self, element: object) -> None:
        self.insert(element, 0)

    def insert_last(self, element: object) -> None:
        self.insert(element, self._count)

    def remove(self, pos: int) -> object:
        if self.is_empty():
            raise UnderflowError()
        if (pos < 0 or pos >= self._count):
            raise IndexError()
        element: object = self._elements[pos]
        for i in range(pos, self._count - 1):
            self._elements[i] = self._elements[i + 1]
        self._count -= 1
        self._elements[self._count] = None
        return element
    
    def remove_first(self) -> object:
        return self.remove(0)
    
    def remove_last(self) -> object:
        return self.remove(self._count - 1)
    
    def get(self, pos: int) -> object:
        if (pos < 0 or pos >= self._count):
            raise IndexError()
        return self._elements[pos]
    
    def search(self, element: object) -> int:
        for i, elm in enumerate(self):
            if elm == element:
                return i
        return -1

    def merge(self, other: ADTList) -> None: #Task 1 Completed
        for item in other:
            self.insert_last(item)
        return self
    
    def sublist(self, i: int, j: int) -> ADTList: #Task 2 Completed
        sublist: ADTList = ArrayList()
        while i <= j:
            sublist.insert_last(self.get(i))
            i += 1
        return sublist
    
    def remove_interval(self, from_index: int, to_index: int) -> int: #Task 3 Completed
        count = 0
        for i in range(to_index - from_index):
            self.remove(from_index)
            count += 1
        return count

    def divide_odd_even(self) -> int:
        new_list: ADTList = ArrayList() #Task 4 Completed
        for item in self:
            if item % 2 == 0:
                new_list.insert_first(item)
            else:
                new_list.insert_last(item)
        self = new_list
        return self
                

lista_other: ADTList = ArrayList()
for i in range(5):
    lista_other.insert_last(i)
if __name__ == "__main__":
    lista: ADTList = ArrayList()
    for i in range(4, -1, -1):
        lista.insert_last(i)
    print(lista)
    print(lista.search(3))
    lista.insert(10, 2)
    print(lista)
    print(lista.remove(2))
    print(lista)
    print("size:", lista.size())
    print("empty:", lista.is_empty())
    print("full:", lista.is_full())
    print("lista_ other:", lista_other) #task 1
    print(lista.merge(lista_other)) #task 1
    print("sublist:",lista.sublist(2,5)) #task 2
    print("removed:",lista.remove_interval(0,4)) #task 3
    for i in lista:
        print(i, end=' ')
    print()
    print(lista.divide_odd_even()) #task 4