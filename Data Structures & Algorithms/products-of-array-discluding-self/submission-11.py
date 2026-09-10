class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        #p: [1, 1, 2, 8]
        #s: [48, 24, 6, 1]

        #p: [1, -1, 0, 0, 0]
        #s: [0, 6, 6, 3, 1]
        start = 1

        for i in range(len(nums)):
            ret[i] *= start
            start *= nums[i]

        start = 1

        for i in range(len(nums)-1, -1, -1):
            ret[i] *= start
            start*=nums[i]

        return ret