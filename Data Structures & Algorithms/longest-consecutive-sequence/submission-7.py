class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashset!!!
        hashset = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in hashset:
                streak = 1
                while((i+streak) in hashset):
                    streak+=1
                longest = max(longest, streak)
        return longest