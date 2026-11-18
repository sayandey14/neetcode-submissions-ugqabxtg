class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []

        def backtrack(i):
            nonlocal nums
            nonlocal ret
            nonlocal path
            if i == len(nums):
                ret.append(path.copy())
                return
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
        
        backtrack(0)
        return ret
