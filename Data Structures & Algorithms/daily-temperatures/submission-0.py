class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #set every value as 0 initially
        stack = [] # gona be a pair so: [temp, index] values in the stack

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #while temps are bigger, u remove stack values
                stackT, stackIdx = stack.pop() #track idx
                res[stackIdx] = i-stackIdx #append idx to res
            stack.append([temp,i]) #add new "greater value"
        return res
            



