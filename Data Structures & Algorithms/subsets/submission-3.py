class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        ret = []

        def dfs(i):
            nonlocal nums
            nonlocal ret
            nonlocal path
            ret.append(path.copy())
            if(i == len(nums)):
                return
            
            for choice in range(i, len(nums)):
                path.append(nums[choice])
                dfs(choice+1)
                path.pop()
        
        dfs(0)

        return ret