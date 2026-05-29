class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        values = self.hashmap.get(key,[]) #[] is a default value 
        l=0
        r=len(values) - 1

        while l<=r:
            mid = (l+r)//2

            if(values[mid][1] > timestamp):
                r = mid-1
            elif(values[mid][1] < timestamp):
                ret = values[mid][0]
                l = mid + 1
            else:
                return values[mid][0]
        return ret

        
