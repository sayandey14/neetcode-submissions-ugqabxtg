class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if(i!=0 and nums[i] == nums[i-1]):
                continue
            l=i+1
            r=len(nums)-1
            while(l<r):
                val = nums[l] + nums[i] + nums[r]

                if(val < 0):
                    l+=1
                elif(val > 0):
                    r-=1
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    while(l<r and nums[l] == nums[l+1]):
                        l+=1
                    l+=1
                    r-=1
                    
        return ret

