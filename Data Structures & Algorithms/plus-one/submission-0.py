class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        length = len(digits)
        fact = 1
        for i in range(length-1,-1,-1):
            num = num + digits[i]*fact
            fact = fact*10
        num +=1
        
        length2 = (str(num))
        ret = list(length2)
        for i in range(len(ret)):
            ret[i] = int(ret[i])
        return ret