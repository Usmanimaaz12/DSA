//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};


// } Driver Code Ends
/*
// structure of the node is as follows

struct Node
{
	int data;
	struct Node* next;
	
	Node(int x){
	    data = x;
	    next = NULL;
	}
	
};

*/
class Solution
{
    public:
    struct Node* makeUnion(struct Node* head1, struct Node* head2)
    {
        Node* curr1 = head1;
        Node* curr2 = head2;
        
        //Using extra space
        vector<int>temp;
        
        while(curr1!=NULL) 
        {
            temp.push_back(curr1->data);
            curr1 = curr1->next;
        }
        
        while(curr2!=NULL) 
        {
            temp.push_back(curr2->data);
            curr2 = curr2->next;
        }
        
        //sort the temp vector
        sort(temp.begin(), temp.end());

        //removing the duplicates
        temp.erase(unique(temp.begin(), temp.end()), temp.end());
        
        //Creating the linked list to return 
        Node* head = new Node(temp[0]);
        Node* tail = head;
        
        //Travering through the list to add the elements to linked list
        for(int i= 1;i<temp.size();i++) 
        {
            tail->next = new Node(temp[i]);
            tail = tail->next;
        }
        
        return head;
    }
};


//{ Driver Code Starts.

struct Node* buildList(int size)
{
    int val;
    cin>> val;
    
    Node* head = new Node(val);
    Node* tail = head;
    
    for(int i=0; i<size-1; i++)
    {
        cin>> val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    cout<< endl;
}


int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        
        cin>>n;
        Node* first = buildList(n);
        
        cin>>m;
        Node* second = buildList(m);
        Solution obj;
        Node* head = obj.makeUnion(first,second);
        printList(head);
    }
    return 0;
}

// } Driver Code Ends