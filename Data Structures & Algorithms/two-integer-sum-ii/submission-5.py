class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        while(l<r):
            if(numbers[l]+numbers[r]==target):
                temp = []
                temp.append(l+1)
                temp.append(r+1)
                return temp
            elif(numbers[l]+numbers[r]<target):
                l+=1
            else:
                r-=1
            
        return []
