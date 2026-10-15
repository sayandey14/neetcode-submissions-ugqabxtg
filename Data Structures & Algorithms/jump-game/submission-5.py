class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        last = len(nums) - 1

        for idx in range(len(nums) - 2, -1, -1):
            if idx + nums[idx] >= last:
                last = idx
        

        return last == 0


        
        

