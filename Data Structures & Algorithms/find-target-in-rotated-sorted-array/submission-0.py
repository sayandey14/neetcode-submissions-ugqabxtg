class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # find pivot 
        while l < r:
            mid = (l + r) // 2
        
            if(nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid
        
        pivot = l


        #find target now 

        def binSearch(left:int, right:int) -> int:
            while left <= right:
                mid = (left+right) // 2
                if(nums[mid] < target):
                    left = mid + 1
                elif (nums[mid] > target):
                    right = mid - 1
                else:
                    return mid
            return -1
        
        l1 = binSearch(0, pivot - 1)
        l2 = binSearch(pivot, len(nums) - 1)
        
        return max(l1, l2)




            