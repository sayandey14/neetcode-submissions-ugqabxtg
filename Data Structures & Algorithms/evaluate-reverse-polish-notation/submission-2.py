class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if(i == '+'):
                temp = int(stack[-2])+int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif(i=='-'):
                temp = int(stack[-2])-int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif(i=='*'):
                temp = int(stack[-2])*int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif(i=='/'):
                temp = int(stack[-2])/int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(i)
            print(stack)
        
        return int(stack[-1])
