class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"}":"{", "]":"[", ")":"("}

        stack = []

        for i in s:
            if i in hashmap:
                if( len(stack) == 0):
                    return False
                if stack[-1] == hashmap[i]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(i)
        
        return (len(stack) == 0)