class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(nums)):
            if((target-nums[i]) in hashset):
                temp = []
                temp.append(hashset.get(target-nums[i]))
                temp.append(i)
                return temp
            hashset[nums[i]] = i
        