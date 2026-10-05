# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #go to half using fast slow ptrs = [1,2,3,(get here) 4,5,6]
        #reverse the list after half = [1,2,3,6,5,4]
        #link using 2 ptr

        #find half
        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        midpoint = slow

        #reverse list after half
        cur = slow.next
        slow.next = None
        prev = None

        while(cur is not None):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        #two pointer linking
        l1 = head
        l2 = prev

        while(l2 is not None):
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
        
        return

