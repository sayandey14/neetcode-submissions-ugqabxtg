class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxstreak = 0

        for i in nums:
            if i-1 not in hashset:
                streak = 1
                while (i+1 in hashset):
                    streak+=1
                    i+=1
                maxstreak = max(maxstreak, streak)
        
        return maxstreak
                