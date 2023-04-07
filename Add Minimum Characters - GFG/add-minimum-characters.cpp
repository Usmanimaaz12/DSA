//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++

class Solution{   
public:
    bool isPalindrome(string st){
        int i=0;
        int j=st.length()-1;
        while(i<=j){
            if(st[i]!=st[j])return 0;
            i++;
            j--;
        }
        return 1;
    }
    int addMinChar(string str){    
        for(int i=str.size()-1;i>=0;i--){
            if(isPalindrome(str.substr(0,i+1)))return (str.length()-i-1);
        }
        return 0;
    }
};

//{ Driver Code Starts.


int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string str;
        cin >> str;
        
        Solution ob;
        cout << ob.addMinChar(str) << endl;
    }
    return 0; 
} 
// } Driver Code Ends