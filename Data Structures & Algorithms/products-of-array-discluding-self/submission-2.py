class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount = 0
        for i in nums:
            if i==0:
                zerocount+=1
        if(zerocount>1):
            return [0]*len(nums)
        
        else:
            prod = 1
            zerocnt = 0
            for i in range(len(nums)):
                if(nums[i]==0):
                    zerocnt+=1
                    continue
                prod*=nums[i]
            if(zerocnt==1):
                for i in range(len(nums)):
                    if(nums[i]==0):
                        nums[i] = prod
                    else:
                        nums[i] = 0
            else:
                for i in range(len(nums)):
                    nums[i] = prod//nums[i]
            

        return nums
