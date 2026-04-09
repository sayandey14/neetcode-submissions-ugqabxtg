class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while(numbers[l]+numbers[r]!=target):
            sumof = numbers[l]+numbers[r]
            if(sumof>target):
                r-=1
            else:
                l+=1
        

        temp = [l+1,r+1]
        return temp