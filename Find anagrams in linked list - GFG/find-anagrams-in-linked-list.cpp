//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    char data;
    struct Node *next;

    Node(char x) {
        data = x;
        next = NULL;
    }
};

void printList(Node *node) {
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

struct Node *inputList() {
    int n; // length of link list
    scanf("%d ", &n);

    char data;
    cin >> data;
    struct Node *head = new Node(data);
    struct Node *tail = head;
    for (int i = 0; i < n - 1; ++i) {
        cin >> data;
        tail->next = new Node(data);
        tail = tail->next;
    }
    return head;
}


// } Driver Code Ends
/*

Definition for singly Link List Node
struct Node
{
    char data;
    Node* next;
    Node(int x) {  data = x;  next = NULL; }
};

You can also use the following for printing the link list.
printList(Node* node);
*/

class Solution {
  public:
    vector<Node*> findAnagrams(struct Node* head, string s) {
        
        vector<Node*> res;
        vector<int> window(26), slidingWindow(26);
        
        for(auto &x: s)window[x-'a']++;
        Node *start = head, *end = head;
        int count = 0;
        
        while(end != NULL) {
            slidingWindow[end->data - 'a']++;
            count++;
            
            if(slidingWindow == window) {
                res.push_back(start);
                start = end->next;
                end->next = NULL;
                end = start;
                count = 0;
                
                for(int i = 0; i < 26; i++)slidingWindow[i] = 0;
            }
            else {
                end = end->next;
                
                if(count >= s.size()) {
                    slidingWindow[start->data - 'a']--;
                    start = start->next;
                }
            }
        }
        
        return res;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {

        struct Node *head = inputList();

        string s;
        cin >> s;

        Solution obj;
        vector<Node *> res = obj.findAnagrams(head, s);

        for (int i = 0; i < res.size(); i++) {
            printList(res[i]);
        }

        if (res.size() == 0) cout << "-1\n";
    }
}

// } Driver Code Ends