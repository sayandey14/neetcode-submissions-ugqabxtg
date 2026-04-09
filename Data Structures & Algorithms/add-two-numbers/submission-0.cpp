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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;

        int carry = 0;
        while(l1 != nullptr || l2 != nullptr || carry !=0){
            int v1;
            int v2;
            if(l1==nullptr){
                v1 = 0;
            }
            else{
                v1 = l1->val;
            }


            if(l2==nullptr){
                v2 = 0;
            }
            else{
                v2 = l2->val;
            }


            int value = v1+v2+carry;

            carry = value/10;
            value = value%10;

            cur->next = new ListNode(value);
            cur = cur->next;
            if(l1==nullptr){
                l1=nullptr;
            }
            else{
                l1 = l1->next;
            }

            if(l2==nullptr){
                l2=nullptr;
            }
            else{
                l2 = l2->next;
            }
        }

        ListNode* ret = dummy->next;
        return ret;
    }
};
