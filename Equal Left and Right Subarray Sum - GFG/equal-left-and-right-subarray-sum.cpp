//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }
 
    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends
class Solution {
  public:
      int equalSum(int N, vector<int> &A) 
    {
        if(N==1)
        {
            return 1;
        }
        vector<int>pref(N,0);
        pref[0]=A[0];
        for(int i=1;i<N;i++)
        {
            pref[i]=pref[i-1]+A[i];
        }
        for(int i=1;i<N;i++)
        {
            if(pref[i-1]==pref[N-1]-pref[i])
            {
                return i+1;
            }
        }
        return -1;
        
        // code here
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int N; 
        scanf("%d",&N);
        
        
        vector<int> A(N);
        Array::input(A,N);
        
        Solution obj;
        int res = obj.equalSum(N, A);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends