class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        after = []


        #before
        beforecnt = 1
        for i in nums:
            before.append(beforecnt)
            beforecnt*=i


        #after
        aftercnt = 1
        for i in range(len(nums)-1, -1, -1):
            after.append(aftercnt)
            aftercnt*=nums[i]

        #ret
        ret = []
        for i in range(len(nums)):
            ret.append(before[i]*after[len(after)-1-i])

        return ret