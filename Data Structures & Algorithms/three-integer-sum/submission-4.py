class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1

            while(l<r):
                cur = nums[i]+nums[l]+nums[r];
                if(cur==0):
                    temp =[nums[i],nums[l],nums[r]]
                    if(temp not in ret):
                        ret.append(temp)
                    l+=1
                    r-=1
                elif(cur<0):
                    l+=1;
                else:
                    r-=1;
        return ret;