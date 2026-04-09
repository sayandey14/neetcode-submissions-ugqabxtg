class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        idx = nums[0]
        for i in range(1,len(nums)):
            if idx == nums[i]:
                return idx
        

        slow, fast = 0,0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow==fast):
                break
        
        slow2 = 0

        while(True):
            slow2 = nums[slow2]
            if(slow2==fast):
                return slow2
            fast = nums[fast];
            if(slow2==fast):
                return slow2

        