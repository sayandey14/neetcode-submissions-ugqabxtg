class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []

        def dfs(i):
            nonlocal target
            nonlocal nums
            nonlocal ret
            if(sum(path) == target):
                ret.append(path.copy())
                return
            if(i>= len(nums)):
                return
            
            for choice in range(i, len(nums)):
                if sum(path) > target:
                    continue
                path.append(nums[choice])
                dfs(choice)
                path.pop()
        dfs(0)
        return ret