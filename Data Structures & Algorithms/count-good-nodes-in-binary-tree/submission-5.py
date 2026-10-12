# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            
            ret = 0
            
            if(root.val >= maxVal):
                ret+=1
            
            maxVal = max(maxVal, root.val)

            ret += dfs(root.left, maxVal)
            ret += dfs(root.right, maxVal)

            return ret
        
        return dfs(root, root.val)
            