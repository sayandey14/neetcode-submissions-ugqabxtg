# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def bfs(root):
            nonlocal ret
            queue = deque()
            if root:
                queue.append(root)
            
            while queue:
                last = len(queue)
                for i in range(last):
                    cur = queue.popleft()

                    if(i == last-1):
                        ret.append(cur.val)
                    
                    if(cur.left):
                        queue.append(cur.left)
                    if(cur.right):
                        queue.append(cur.right)
                    
        bfs(root)
        return ret