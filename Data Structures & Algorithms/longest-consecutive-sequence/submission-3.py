class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if(nums == []):
            return 0
        maxnum = max(nums)
        minnum = min(nums)


        #hashmap
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1+hashmap.get(nums[i],0)

        print(hashmap)
        print("max:", maxnum)
        print("min:", minnum)

        maxstreak = 0
        streak = 0
        for i in range(maxnum,minnum-1, -1):
            if(i in hashmap):
                streak+=1
            else:
                maxstreak = max(maxstreak, streak)
                streak = 0
        maxstreak = max(maxstreak,streak)
        
        return maxstreak
            
