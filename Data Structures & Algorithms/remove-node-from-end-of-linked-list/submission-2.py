# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None

        count = 0

        while(count < n and fast is not None):
            fast = fast.next
            count+=1
        if(fast is None):
            return head.next
        
        while(fast is not None):
            prev = slow
            slow = slow.next
            fast = fast.next
        
        #delete
        prev.next = slow.next

        return head