# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret = []
        
        def dfs(root):
            #inorder
            nonlocal ret
            if not root:
                return
            
            dfs(root.left)
            ret.append(root.val)
            dfs(root.right)
        
        dfs(root)
        print(ret) 
        if(len(ret) > 0):
            for i in range(1, len(ret)):
                if ret[i] <= ret[i-1]:
                    return False
            return True
        else:
            return True 
        