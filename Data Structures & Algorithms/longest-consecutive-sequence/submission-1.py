class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        maxseq = 1
        temp = 1
        for i in range(len(nums)-1):
            if(nums[i+1] == nums[i]):
                continue
            if(nums[i+1] == nums[i]+1):
                temp+=1
            else:
                maxseq=max(temp,maxseq)
                temp=1

        return max(maxseq,temp)