class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []
        nums.sort()

        def dfs(i):
            nonlocal nums
            nonlocal ret
            nonlocal path
            ret.append(path.copy())
            if i == len(nums):
                return
            for choice in range(i, len(nums)):
                if(choice > i and nums[choice] == nums[choice-1]):
                    continue
                path.append(nums[choice])
                dfs(choice+1)
                path.pop()
        
        dfs(0)
        return ret
