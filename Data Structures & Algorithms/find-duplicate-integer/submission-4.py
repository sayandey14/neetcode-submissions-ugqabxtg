class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        if(len(nums)==2):
            return nums[0]
        n=len(nums)

        while True:
            if(fast==n-1):
                fast = 1
            elif(fast==n-2):
                fast=0
            else:
                fast+=2
                if(slow==n-1):
                    slow=0
                else:
                    slow+=1
            if(nums[fast]==nums[slow] and fast!=slow):
                print(fast, slow)
                return nums[fast]
        return 0

            