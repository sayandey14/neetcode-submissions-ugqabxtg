class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0]*len(temperatures)
        stack = [] #(temp,idx)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                ind = stack[-1][1]
                ret[ind] = i-ind
                stack.pop()
            stack.append((temp,i))
        return ret