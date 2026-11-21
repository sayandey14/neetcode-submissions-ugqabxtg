class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freq list: for example, if we have 2,2,2,4,5,6,6,6, then it will be 2:3, 4:1, 5:1, 6:3, etc

        frequency = {}

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0)
        

        reverse = {}

        for key,v in frequency.items():
            reverse[v] = []
        
        for key,v in frequency.items():
            reverse[v].append(key)
        
        print(reverse)
        ret = []
        for i in range(len(nums),-1,-1):
            if i in reverse:
                for j in reverse[i]:
                    print(ret)
                    if (len(ret) == k):
                        return ret
                    ret.append(j)

        return ret