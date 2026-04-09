class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp = []
        
        for i in range(len(position)):
            temp.append([position[i], speed[i]])
        #temp now has: [[p1, s1], [p2, s2], [p3, s3]...]

        temp.sort(reverse=True)

        time = []
        for i in range(len(temp)):
            cur = (target-temp[i][0])/temp[i][1]
            time.append(cur)
        
        stack = []

        for i in time:
            if not stack:
                stack.append(i)
            
            else:
                if(i > stack[-1]):
                    stack.append(i)
        
        return len(stack)