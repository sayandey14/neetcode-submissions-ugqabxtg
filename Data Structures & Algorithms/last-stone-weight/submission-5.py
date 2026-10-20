class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
                x = heapq.heappop(stones)
                y = heapq.heappop(stones)
                x = -1*x
                y = -1*y
                if x > y:
                    heapq.heappush(stones, -1*(x-y))
                elif(y > x):
                    heapq.heappush(stones, -1*(y-x))

        return abs(stones[0]) if stones else 0