class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []

        def backtrack(i):
            nonlocal nums
            nonlocal ret
            nonlocal path
            ret.append(path.copy())
            if i == len(nums):
                return
            for choice in range(i, len(nums)):
                path.append(nums[choice])
                backtrack(choice+1)
                path.pop()
        
        backtrack(0)
        return ret
