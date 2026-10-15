class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxx = 0
        temp_max = float("-infinity")
        for i in nums:
            temp_max = max(temp_max, i)
            cur+=i
            maxx = max(maxx, cur)
            if(cur < 0):
                cur = 0
        
        if(temp_max < 0):
            return temp_max
        return maxx
