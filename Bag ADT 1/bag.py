class bag:
    def __init__(self):
        self._items  = []

    def Insert(self, item):
        if self.Exists(item):
            return False
        self._items.append(item)
        return True
    
    def Exists(self, item):
        for x in self._items:
            if x == item:
                return True
        return False

    def Size(self):
        return len(self._items)

    def __iter__(self, item):
        for item in self._items:
            yield item
    
    def Delete(self, item):
        for i, x in enumerate(self._items):
            if x == item:
                del self._items[i]
                return True
        return False
    
    def Retrive(self, item):
        for x in self._items:
            if x == item:
                return x
        return False



