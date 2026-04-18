class Solution:
    def findMin(self, nums: List[int]) -> int:
        #sorted

        if nums[0] <= nums[-1] :
            return nums[0]
        
        #not sorted
        l=0
        r = len(nums) - 1

        while(l<=r):
            mid = (l+r)//2
            if(nums[mid+1] > nums[mid] and nums[mid] > nums[0]):
                l = mid
            elif(nums[mid+1] > nums[mid] and nums[mid] < nums[0]):
                r = mid
            else:
                return nums[mid+1]
        
        return -1