# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #iterative
        cur = ListNode()
        head = cur

        iter1 = list1
        iter2 = list2

        while(iter1 is not None or iter2 is not None):
            if(iter1 is None):
                cur.next = iter2
                return head.next
            elif(iter2 is None):
                cur.next = iter1
                return head.next
            else:
                if(iter1.val<=iter2.val):
                    cur.next = iter1
                    iter1=iter1.next
                else:
                    cur.next = iter2
                    iter2=iter2.next
                cur=cur.next
        
        return head.next
        