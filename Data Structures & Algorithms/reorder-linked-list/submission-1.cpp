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
    void reorderList(ListNode* head) {
        /**
            turtoise and hare RAHH
            reverse LL at middle RAHH
            two pointer method RAHH
        **/

        //find midpoint using fast and slow pointers

        ListNode* fast = head;
        ListNode* slow = head;

        while(fast!= nullptr && fast->next!=nullptr && fast->next->next!=nullptr){
            slow=slow->next;
            fast=fast->next->next;
        }

        //reverse everything after slow basically


        //reverse
        ListNode* cur = slow->next;
        ListNode* prev = nullptr;
        while(cur!=nullptr){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }

        //set proper
        slow->next = nullptr;


        //2 ptrs now: we have [0,1,2,3,6,5,4]
        ListNode* l = head;
        ListNode* r = prev;
        ListNode* temp = head;
        while(r != nullptr){
            temp = l->next;
            l->next = r;
            l=temp;
            temp = r->next;
            r->next = l;
            r=temp;
        }
    }
};
