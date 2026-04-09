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

    bool same(TreeNode* root, TreeNode* subRoot){
        if(!root && !subRoot){
            return true;
        }

        if(root != nullptr and subRoot != nullptr and root->val == subRoot->val){
            return same(root->left, subRoot->left) && same(root->right, subRoot->right);
        }

        return false;
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(same(root, subRoot)){
            return true;
        }

        if(!subRoot){
            return true;
        }

        if(!root){
            return false;
        }
        
        return (false || isSubtree(root->right, subRoot) || isSubtree(root->left, subRoot));
    }
};
