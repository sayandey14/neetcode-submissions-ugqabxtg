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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* prev = nullptr;
        ListNode* slow = head;
        ListNode* fast = head;

        //move fast n spaces:

        for(int i=0;i<n;i++){
            fast=fast->next;
        }
        

        //check if end is reached:

        if(fast==nullptr){
            return head->next;
        }

        //move both ptrs:

        while(fast!=nullptr){
            prev=slow;
            slow=slow->next;
            fast=fast->next;
        }

        //delete
        prev->next=slow->next;
        delete slow;
        return head;
        
    }
};
