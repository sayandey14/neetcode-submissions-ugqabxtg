class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if(i=="+"):
                temp = stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif(i=="-"):
                temp = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)

            elif(i=="*"):
                temp = stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)

            elif(i=="/"):
                temp = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(int(i))
        return stack[-1]

            

