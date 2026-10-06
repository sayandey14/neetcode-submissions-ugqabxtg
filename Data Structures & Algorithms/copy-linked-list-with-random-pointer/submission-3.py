class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # Pass 1: A -> A' -> B -> B' -> ...
        cur = head
        while cur is not None:
            nxt = cur.next
            copy = Node(cur.val)

            cur.next = copy
            copy.next = nxt

            cur = nxt

        # Pass 2: set random pointers
        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next

            cur = cur.next.next

        # Pass 3: separate the lists
        cur = head
        copy_head = head.next

        while cur is not None:
            copy = cur.next

            cur.next = copy.next

            if copy.next is not None:
                copy.next = copy.next.next

            cur = cur.next

        return copy_head