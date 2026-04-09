class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        for i in range(len(nums)-2):
            cur = nums[i]
            l = i+1
            r = len(nums)-1

            while(l<r):
                if(cur+nums[l]+nums[r] == 0):
                    temp = [cur,nums[l],nums[r]]
                    if(temp not in ret):
                        ret.append(temp)
                    l+=1
                    r-=1
                elif(cur+nums[l]+nums[r] >0):
                    r-=1
                else:
                    l+=1
        return ret