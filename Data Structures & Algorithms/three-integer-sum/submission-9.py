class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            l = i+1
            r=len(nums)-1

            while(l<r):
                tar = nums[i]+nums[l]+nums[r]
                if(tar==0):
                    ret.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while(nums[l-1] == nums[l] and l<r):
                        l+=1
                    while(nums[r+1]==nums[r] and l<r):
                        r-=1
                elif(tar>0):
                    r-=1
                
                else:
                    l+=1
        
        return ret
