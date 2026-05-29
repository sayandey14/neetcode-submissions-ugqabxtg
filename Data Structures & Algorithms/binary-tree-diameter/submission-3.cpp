/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    //find the max left most and right most for each node. so run dfs on each node and calculate left and right and subtract
    int dfs(TreeNode* root, int& ret){
        if(!root){
            return 0;
        }
        else{
            int left = dfs(root->left, ret);
            int right = dfs(root->right, ret);
            ret = max(left + right, ret);
            return (1 + max(left, right));
        }
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ret = 0;
        dfs(root, ret);
        return ret;
    }
};
