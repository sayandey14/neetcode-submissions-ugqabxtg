class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)!=1 or len(stones)!=0):
            stones.sort()
            if(len(stones)==1):
                return stones[0]
            elif(len(stones) == 2 and stones[0]==stones[1]):
                return 0
            else:
                diff = stones[-1]-stones[-2]
                if(diff == 0):
                    stones.pop(-1)
                    stones.pop(-1)
                else:
                    stones.pop(-1)
                    stones[-1] = diff
        if(len(stones)==0):
            return 0
        else:
            return stones[0]