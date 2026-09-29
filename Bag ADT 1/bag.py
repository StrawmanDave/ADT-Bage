class bag:
    def __init__(self):
        self.items = []

    def insert(self, item):
        if self.exists == True:
            return False
        self.append(item)

    def delete(self, item):
        if self.exists == True:
            self.pop(item)
            return True
        return False # if item is not in list
    
    def exists(self, item):
        is_there = False
        for x in self:
            if item == x:
                is_there = True
        return is_there

    def retrive(self, item):
        for x in self:
            if item == x:
                return x
        return False

    def __iter__(self):
        for item in self:
            yield item

    def size(self):
        size = 0
        for i in range(len(self)):
            size += 1
        return size