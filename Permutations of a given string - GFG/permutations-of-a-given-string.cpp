//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution

{

     private:

        void solve(int ind,string &S, set<string>&s){

            if(ind == S.length()){

                s.insert(S);

                return;

            }

            

            for(int i = ind;i<S.length();i++){

                swap(S[ind],S[i]);

                solve(ind+1,S,s);

                swap(S[ind],S[i]);

            }

        }

    public:

        vector<string>find_permutation(string S)

        {

            // Code here there

            vector<string>ans;

            set<string>s;

            solve(0,S,s);

            

            for(auto it:s){

                ans.push_back(it);

            }

            return ans;

        }

};



//{ Driver Code Starts.
int main(){
    int t;
    cin >> t;
    while(t--)
    {
	    string S;
	    cin >> S;
	    Solution ob;
	    vector<string> ans = ob.find_permutation(S);
	    for(auto i: ans)
	    {
	    	cout<<i<<" ";
	    }
	    cout<<"\n";
    }
	return 0;
}

// } Driver Code Ends