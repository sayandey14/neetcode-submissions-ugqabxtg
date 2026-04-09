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
    vector<int> nums;
    void dfs(TreeNode*root){
        if(!root){
            return;
        }

        dfs(root->left);
        nums.push_back(root->val);
        dfs(root->right);
    }

    int kthSmallest(TreeNode* root, int k) {
        dfs(root);
        return nums[k-1];
    }
};
