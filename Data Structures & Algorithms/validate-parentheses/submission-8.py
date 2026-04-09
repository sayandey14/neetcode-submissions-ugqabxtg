class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)==1 or len(s)==0):
            return False

        hashmap = {
            "}": "{",
            "]": "[",
            ")": "("
        } 

        stack = []

        for i in s:
            if i in hashmap:
                if(not stack):
                    return False
                if(stack[-1]==hashmap[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        
        return not stack