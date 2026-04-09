class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                input1 = int(stack.pop())
                input2 = int(stack.pop())
                stack.append(input1+input2)

            elif i == "-":
                input1 = int(stack.pop())
                input2 = int(stack.pop())
                stack.append(input2-input1)

            elif i == "*":
                input1 = int(stack.pop())
                input2 = int(stack.pop())
                stack.append(input1 * input2)
                
            elif i == "/":
                input1 = int(stack.pop())
                input2 = int(stack.pop())
                stack.append(input2/input1)
                
            else:
                stack.append(i)

        return int(stack[-1])