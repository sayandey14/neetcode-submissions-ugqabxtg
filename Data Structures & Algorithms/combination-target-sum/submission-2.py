class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        path = []
        def dfs(i, total):
            nonlocal target
            nonlocal nums
            nonlocal ret

            if(total == target):
                ret.append(path.copy())
                return
            if(i>= len(nums)):
                return
            
            for choice in range(i, len(nums)):
                if total > target:
                    continue
                path.append(nums[choice])
                total += nums[choice]
                dfs(choice, total)
                total -= path.pop()
        dfs(0, 0)
        return ret