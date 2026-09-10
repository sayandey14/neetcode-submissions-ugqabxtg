class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxStreak = 0

        for i in nums:
            if(i-1 not in hashset):
                streak = 0
                while(i in hashset):
                    streak +=1
                    i+=1
                maxStreak = max(streak, maxStreak)
        return maxStreak
