class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while(len(stack) > 0 and temperatures[i]>temperatures[stack[-1]]):
                prev_index = stack.pop()
                ret[prev_index] = i - prev_index
            
            stack.append(i)
        print(ret)

        return ret