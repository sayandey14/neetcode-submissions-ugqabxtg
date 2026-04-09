class Solution:
    def isValid(self, s: str) -> bool:

        if(len(s)==1):
            return False
        stack = []

        hashmap = { ")" : "(",
                    "]" : "[",
                    "}" : "{"}
        
        for i in s:
            if i in hashmap:
                if(stack and stack[-1]!=hashmap[i]):
                    return False
                else:
                    if(not stack):
                        return False
                    stack.pop()
            
            else:
                stack.append(i)

        


        return not stack

        

