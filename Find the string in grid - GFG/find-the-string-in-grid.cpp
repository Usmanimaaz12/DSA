//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
public:
    bool dfs(vector<vector<char>>& grid, int i, int j, bool vis[50][50],string word, int flag, string &match)
       {
            if (match == word) return true;
            if(i<0 || i>=grid.size() || j<0 || j>=grid[0].size() || vis[i][j]==true) return false ;
                
            match+= grid[i][j];
            bool wordexist = false;
            vis[i][j]= true;
            
            if(flag==1) wordexist|=dfs(grid,i+1,j,vis,word, flag, match);
            if(flag==2) wordexist|=dfs(grid,i-1,j,vis,word, flag, match);
            if(flag==3) wordexist|=dfs(grid,i,j+1,vis,word, flag, match);
            if(flag==4) wordexist|=dfs(grid,i,j-1,vis,word, flag, match);
            if(flag==5) wordexist|=dfs(grid,i+1,j-1,vis,word, flag, match);
            if(flag==6) wordexist|=dfs(grid,i-1,j+1,vis,word, flag, match);
            if(flag==7) wordexist|=dfs(grid,i+1,j+1,vis,word, flag, match);
            if(flag==8) wordexist|=dfs(grid,i-1,j-1,vis,word, flag, match);
            
            vis[i][j]= false;
            return wordexist;
       }
 
vector<vector<int>>searchWord(vector<vector<char>>grid, string word){
 
        bool vis[50][50];
        memset(vis,false, sizeof(vis));
        int n= grid.size();
        int m= grid[0].size();
        vector<vector<int>> ans;
        
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(grid[i][j]==word[0]){
                    for(int k=1; k<=8; ++k){
                        string match = "";
                        if(dfs(grid, i, j, vis,word,k, match)){
                            ans.push_back({i,j});
                            break;
                        }
                    }
                }
            }
        }
        return ans;     
}
};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m;
		cin >> n >> m;
		vector<vector<char>>grid(n, vector<char>(m,'x'));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++)
				cin >> grid[i][j];
		}
		string word;
		cin >> word;
		Solution obj;
		vector<vector<int>>ans = obj.searchWord(grid, word);
		if(ans.size() == 0)
		{
		    cout<<"-1\n";
		}
		else
		{
		    for(auto i: ans){
			for(auto j: i)
				cout << j << " ";
			cout << "\n";
		    }
		}
		
		
	}
	return 0;
}
// } Driver Code Ends