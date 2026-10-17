class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ret = float('-inf')

        def dfs(node):
            nonlocal max_ret
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            max_ret = max(max_ret, node.val + left + right)  # path bending here
            return node.val + max(left, right)               # path continuing up

        dfs(root)
        return max_ret