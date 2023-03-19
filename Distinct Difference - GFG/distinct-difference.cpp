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
    vector<int> getDistinctDifference(int n, vector<int> &a) {
        // code here
        set<int>st;
        vector<int>l(n,0);
        vector<int>r(n,0);
        vector<int>ans;
        for(int i=0;i<n;i++){
            l[i]=st.size();
            st.insert(a[i]);
        }
        st.clear();
        for(int i=n-1;i>=0;i--){
            r[i]=st.size();
            st.insert(a[i]);
        }
        for(int i=0;i<n;i++){
            ans.push_back(l[i]-r[i]);
        }
        return ans;
        
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
        vector<int> res = obj.getDistinctDifference(N, A);
        
        Array::print(res);
        
    }
}

// } Driver Code Ends