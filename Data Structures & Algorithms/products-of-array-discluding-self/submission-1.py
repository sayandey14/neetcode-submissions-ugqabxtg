class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []
        product = 1
        numZero = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                product*=nums[i]
            else:
                numZero+=1
        
        if(numZero>1):
            return [0]*len(nums)
        
        if(numZero==1):
            for i in range(len(nums)):
                if(nums[i]!=0):
                    temp.append(0)
                else:
                    temp.append(product)

        else:
            for i in range(len(nums)):
                if(nums[i]==0):
                    temp.append(product)
                else:
                    temp.append(product//nums[i])
        

        
        return temp
        