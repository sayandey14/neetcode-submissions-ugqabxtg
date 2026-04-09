class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = defaultdict(int)

        for i in range(len(nums)):
            hashset[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target-nums[i]
            if((diff in hashset) and (i!=hashset[diff])):
                return [i,hashset[diff]]
            