class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while(len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]):
                prev_idx = stack.pop()
                ret[prev_idx] = i - prev_idx
            stack.append(i)
        
        return ret