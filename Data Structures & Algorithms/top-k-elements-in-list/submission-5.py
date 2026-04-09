class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1+freq.get(i,0)
        
        print(freq)

        reverse = {}
        for i in freq.values():
            reverse[i] = []

        for i in freq:
            reverse[freq[i]].append(i)
        
        print(reverse)

        cnt=0
        ret = []

        for i in range(len(nums), -1, -1):
            if i in reverse:
                for value in reverse[i]:
                    ret.append(value)
                    if(len(ret)==k):
                        return ret
        return ret


        