class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Stream the rest of the elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
                
        # The root is the kth largest element
        return min_heap[0]