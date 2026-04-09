class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        longest = 0

        for i in hashset:
            if((i-1) not in hashset):
                streak = 1
                while((i+1) in hashset):
                    streak+=1
                    i+=1
                longest = max(streak, longest)

        return longest