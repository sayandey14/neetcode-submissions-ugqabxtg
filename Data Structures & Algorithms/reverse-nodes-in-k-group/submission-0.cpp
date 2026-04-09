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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* temp = head;
        while(temp!=nullptr){
            count+=1;
            temp=temp->next;
        }

        if(count<k){
            return head;
        }

        ListNode* stop = head;
        int temp_cnt = 0;
        while(temp_cnt<k){
            stop=stop->next;
            temp_cnt+=1;
        }
        
        ListNode* cur = head;
        ListNode* prev = reverseKGroup(stop, k);

        while(cur!=stop){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev=cur;
            cur=temp;
        }

        return prev;
    }
};
