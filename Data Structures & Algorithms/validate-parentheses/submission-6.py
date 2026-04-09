class Solution:
    def isValid(self, s: str) -> bool:

        if(len(s)==0 or len(s)==1):
            return False

        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if(i in hashmap):
                if(stack and hashmap[i] == stack[-1]):
                    stack.pop()
                else:
                    return False         
            else:
                stack.append(i)
        
        return not stack