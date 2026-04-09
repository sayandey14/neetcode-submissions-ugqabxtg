class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = sorted(nums)
        length = len(nums)
        for i in range(0,(length-1)):
            if(temp[i] == temp[i+1]):
                return True
        return False
         