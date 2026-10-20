class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        heap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            if distance not in distances:
                distances[distance] = []
                heap.append(distance)
            distances[distance].append([x,y])
    
        heapq.heapify(heap)

        ret = []
        count = k
        for i in range(k):
            distance = heapq.heappop(heap)
            point = distances[distance]
            for i in point:
                ret.append(i)
                count-=1
                if count == 0:
                    return ret
        
        return ret
