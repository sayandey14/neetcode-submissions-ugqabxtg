class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {'}':'{', ']':'[', ')':'('}

        for i in s:
            if i in hashmap and stack:
                if(stack[-1] == hashmap[i]):
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        

        return len(stack) == 0


        
