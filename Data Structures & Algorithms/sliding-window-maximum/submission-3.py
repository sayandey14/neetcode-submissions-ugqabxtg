class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #dequeue

        dq = deque()
        l=0
        r=0
        ret = []
        
        while(r<len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if(dq[0] < l):
                dq.popleft()
            
            while(r-l+1 >= k):
                ret.append(nums[dq[0]])
                l+=1
            r+=1
        
        return ret