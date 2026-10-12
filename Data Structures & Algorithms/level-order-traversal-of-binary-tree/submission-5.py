# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        def bfs(root):
            nonlocal ret
            queue = deque()

            if(root):
                queue.append(root)
            
            while queue:
                l = []
                for i in range(len(queue)):
                    cur = queue.popleft()

                    l.append(cur.val)

                    if(cur.left):
                        queue.append(cur.left)
                    if(cur.right):
                        queue.append(cur.right)
                ret.append(l)
        
        bfs(root)
        return ret