class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_range(lo, hi):  # inclusive range [lo, hi]
            memo = {}
            def dfs(i):
                if i > hi:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
                return memo[i]
            return max(dfs(lo), dfs(lo + 1))

        return max(rob_range(0, n - 2), rob_range(1, n - 1))