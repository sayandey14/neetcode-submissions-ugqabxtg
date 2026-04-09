/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* helper(ListNode* first, ListNode* second, int carry){
        if(first==nullptr && second==nullptr){
            if(carry == 1){
                ListNode* last = new ListNode(1);
                return last;
            }
            return nullptr;
        }
        else if (first == nullptr) {
            ListNode* last = new ListNode();
            int temp = second->val + carry;
            last->val = temp % 10;
            last->next = helper(nullptr, second->next, temp / 10);
            return last;
        }
        else if(second == nullptr){
            if(first->val == 9){
                first->val = 0;
                first->next = helper(first->next, nullptr, 1);
            }
            else{
                first->val+=carry;
                first->next = helper(first->next, nullptr, 0);
            }
        }
        else{
            int temp = first->val + second->val + carry;
            int carry_ret = 0;
            if(temp>9){
                first->val = temp%10;
                carry_ret += 1;
            }
            else{
                first->val = temp;
            }
            first->next = helper(first->next, second->next, carry_ret);
        }

        return first;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return helper(l1, l2, 0);
    }
};
