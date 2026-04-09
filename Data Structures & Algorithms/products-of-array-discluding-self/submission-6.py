class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,4,6] --> before: [1,1,2,8]
        #[1,2,4,6] --> after: [1,6,24,48]

        before = []
        after = []

        cnt = 1
        for i in nums:
            before.append(cnt)
            cnt*=i
        print(before)

        
        cnt = 1
        for i in range(len(nums)-1, -1, -1):
            after.append(cnt)
            cnt*=nums[i]
        print(after)


        ret = []

        for i in range(len(nums)):
            ret.append(before[i] * after[len(nums)-i-1])
        return ret

