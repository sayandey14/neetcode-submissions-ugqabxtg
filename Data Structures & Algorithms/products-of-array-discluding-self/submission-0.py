class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if(j!=i):
                    product*=nums[j]
            temp.append(product)
        return temp
        