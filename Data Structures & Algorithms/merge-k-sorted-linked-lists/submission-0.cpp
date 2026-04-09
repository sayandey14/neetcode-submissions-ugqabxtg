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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(!list1 && !list2){
            return nullptr;
        }
        if(!list1 && list2){
            return list2;
        }
        if(!list2 && list1){
            return list1;
        }
        if(list1->val > list2->val){
            list2->next=mergeTwoLists(list1,list2->next);
            return list2;
        }
        else{
            list1->next=mergeTwoLists(list2,list1->next);
            return list1;
        }
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0){
            return nullptr;
        }

        if(lists.size() == 1){
            return lists[0];
        }
        if(lists.size()==2){
            return mergeTwoLists(lists[0], lists[1]);
        }
        else{
            ListNode* temp = mergeTwoLists(lists[0], lists[1]);
            for(int i=2;i<lists.size();i++){
                temp = mergeTwoLists(temp, lists[i]);
            }
            return temp;
        }
    }
};
