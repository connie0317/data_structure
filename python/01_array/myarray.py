class MyArray: 
    
    def __init__(self, length:int):
        self._data = []
        self._length = length 
    
    def __getitem__(self, position:int): 
        return self._data[position]
    
    def __setitem__(self, index:int, value: object):
        self._date[index] = value 

    def __len__(self, ):
        return len(self._data)
    
    def __iter__(self):
        for item in self._data:
            yield item
    
    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None
        
    def delete(self, index: int) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False
        
    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._length:
            return False
        else:
            return self._data.insert(index, value)
    
    def print_all(self):
        for item in self:
            print(item)
    
def test_myarray():
    array = MyArray(5)
    array.insert(0, 2)
    array.insert(0, 1)
    array.insert(1, 3)
    array.insert(3, 6)
    array.insert(3, 5)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 3
    assert array.delete(4) is True
    array.print_all()


if __name__ == "__main__":
    test_myarray()
        
    
    
