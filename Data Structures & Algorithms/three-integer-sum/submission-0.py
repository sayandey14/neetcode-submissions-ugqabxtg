class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i in range(len(nums)-2):
            if(i>0 and nums[i-1] == nums[i]):
                continue
            left = i+1
            right = len(nums)-1
            while(right>left):
                if(nums[i]+nums[left]+nums[right] == 0):
                    temp = [nums[i], nums[left], nums[right]]
                    ret.append(temp)
                    while(right>left and nums[left+1] == nums[left]):
                        left+=1
                    while(right>left and nums[right-1] == nums[right]):
                        right-=1
                    left+=1
                    right-=1
                elif(nums[i]+nums[left]+nums[right] > 0):
                    right-=1
                else:
                    left+=1
        return ret

