class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        #p: [1, 1, 2, 8]
        #s: [48, 24, 6, 1]

        #p: [1, -1, 0, 0, 0]
        #s: [0, 6, 6, 3, 1]
        start = 1

        for i in nums:
            prefix.append(start)
            start*=i

        start = 1

        for i in range(len(nums)-1, -1, -1):
            suffix.append(start)
            start*=nums[i]

        ret = []

        for i in range(len(nums)):
            ret.append(prefix[i] * suffix[len(nums)-1-i])
        return ret