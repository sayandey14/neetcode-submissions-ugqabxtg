class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        prefix = [0]*length
        postfix = [0]*length

        prefix[0] = 1
        postfix[length-1] = 1

        for i in range(1,length):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(length-2,-1,-1):
            postfix[i] = nums[i+1]*postfix[i+1]
        
        for i in range(length):
            res[i] = prefix[i]*postfix[i]
        return res
