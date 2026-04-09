/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head==nullptr){
            return nullptr;
        }
        //add replacements A->B->C --> A->A'->B->B'->C->C'
        Node* temp = head;
        while(temp!=nullptr){
            Node* replacement = new Node(temp->val);
            replacement->next = temp->next;
            temp->next = replacement;
            temp = replacement->next;
        }
        //set ret value
        Node* ret = head->next;

        //make the ->randoms match by abusing the fact that its right after
        temp = head;
        while(temp!=nullptr){
            if(temp->random!=nullptr){
                temp->next->random = temp->random->next;
            }
            temp = temp->next->next;
        }

        //restoring order to original list + extract copy to new seperate list
        temp = head;

        while(temp != nullptr){
            Node* placeholder = temp->next; //extract placeholder
            temp->next = placeholder->next; //return order

            if(placeholder->next != nullptr){
                placeholder->next = placeholder->next->next; //set for the copied list 
            }
            temp = temp->next;

        }

        return ret;

    }
};
