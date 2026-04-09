class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        temp = self.cache.pop(key)
        self.cache[key] = temp
        return temp

    def put(self, key: int, value: int) -> None:
        if (key in self.cache):
            self.cache.pop(key)
            self.cache[key] = value
        elif(len(self.cache)<self.cap):
            self.cache[key] = value
        else:
            self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value
        


        
