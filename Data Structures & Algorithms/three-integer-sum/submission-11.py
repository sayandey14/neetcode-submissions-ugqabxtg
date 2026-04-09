class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            #hazards
            if(i>0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r = len(nums)-1

            while(l<r):
                summ = nums[l] + nums[r] + nums[i]
                
                if(summ == 0):
                    ret.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
                    while(l<r and nums[r] == nums[r+1]):
                        r-=1
                elif(summ < 0):
                    l+=1
                else:
                    r-=1
        
        return ret