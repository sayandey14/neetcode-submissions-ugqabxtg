class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []

        dqueue = deque()
        l = 0
        r = 0

        while(r < len(nums)):
            #pop smaller values from the queue (queue = [6,5], if you add 8, then remove 6 and 5)
            while dqueue and nums[dqueue[-1]] < nums[r]: #while deque not empty and dequene "largest" val is smaller than current value
                dqueue.pop()
            dqueue.append(r) # if you add queue =[6, 5] and you add 3, you are free to 

            if l > dqueue[0]: #note dequeue stores indexes, so if the leftmost(max) value is out of bounds cuz l is the window, we pop it 
                dqueue.popleft()
            #append when window size is k
            while(r-l+1 >= k):
                ret.append(nums[dqueue[0]])
                l+=1
            r+=1
        
        return ret
            


