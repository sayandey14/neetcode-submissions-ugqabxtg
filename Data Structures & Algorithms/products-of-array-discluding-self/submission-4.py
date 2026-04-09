class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        after = []

        #before 

        prodcnt = 1
        for i in range(len(nums)):
            before.append(prodcnt)
            prodcnt*=nums[i]
        print(before)


        #after 

        prod = 1

        for i in range(len(nums)-1,-1,-1):
            after.append(prod)
            prod*=nums[i]
        after.reverse()
        print(after)


        ret = []

        for i in range(len(nums)):
            ret.append(after[i]*before[i])



        return ret
    


        