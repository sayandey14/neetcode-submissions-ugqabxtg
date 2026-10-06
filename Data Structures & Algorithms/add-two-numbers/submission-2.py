# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #iter
        carry = 0
        dummy = ListNode()
        cur = dummy
        while(l1 is not None or l2 is not None or carry!=0):
            l1_val = 0
            l2_val = 0
            if(l1 is not None):
                l1_val = l1.val
            if(l2 is not None):
                l2_val = l2.val
            
            summ = carry + l1_val + l2_val

            val = summ%10
            carry = summ//10

            cur.next = ListNode(val)
            cur = cur.next
            if(l1 is not None):
                l1 = l1.next
            if(l2 is not None):
                l2 = l2.next
        
        return dummy.next

