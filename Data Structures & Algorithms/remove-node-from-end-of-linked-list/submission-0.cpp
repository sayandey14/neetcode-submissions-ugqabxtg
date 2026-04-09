class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;
        
        // Move fast pointer n steps ahead
        for (int i = 0; i < n; i++) {
            fast = fast->next;
        }
        
        // If fast reached the end, remove the head node
        if (fast == nullptr) {
            return head->next;
        }
        
        // Move both fast and slow pointers until fast reaches the end
        while (fast != nullptr) {
            prev = slow;
            slow = slow->next;
            fast = fast->next;
        }
        
        // Now slow points to the node to be removed
        prev->next = slow->next;
        delete slow;
        
        return head;
    }
};
