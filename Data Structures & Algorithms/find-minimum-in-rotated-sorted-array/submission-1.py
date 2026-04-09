class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r = len(nums) - 1
        ret = nums[0]
        while(l<=r):
            if(nums[l] < nums[r]):
                ret = min(ret, nums[l])


            mid = l+((r-l)//2)
            ret = min(ret, nums[mid])
            if(nums[mid] >= nums[l]):
                l = mid + 1 #left side is sorted
            else:
                r = mid - 1 #right side is sorted
        return ret;