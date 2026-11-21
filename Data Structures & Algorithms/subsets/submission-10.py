class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        path = []

        def dfs(i):
            ret.append(path.copy())
            if i == len(nums):
                return
            
            for c in range(i,len(nums)):
                path.append(nums[c])
                dfs(c+1)
                path.pop()
        
        dfs(0)
        return ret