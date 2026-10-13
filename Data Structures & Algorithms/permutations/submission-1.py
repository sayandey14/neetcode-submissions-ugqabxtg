class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []

        path = []

        def dfs():
            nonlocal nums
            nonlocal ret
            nonlocal path
            if(len(path) == len(nums)):
                ret.append(path.copy())
                return
            
            for choice in range(len(nums)):
                if(nums[choice] in path):
                    continue
                path.append(nums[choice])
                dfs()
                path.pop()
        
        dfs()
        return ret
            