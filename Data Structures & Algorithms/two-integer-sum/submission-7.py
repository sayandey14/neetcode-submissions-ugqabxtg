class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()

        for i in range(len(nums)):
            tar = target-nums[i]
            if(tar in hashmap):
                temp = [hashmap[tar], i]
                return temp;
            hashmap[nums[i]] = i
        return 0