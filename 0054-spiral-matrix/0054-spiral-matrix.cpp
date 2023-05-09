class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int dir=0,left=0,top=0,down=matrix.size()-1,right=matrix[0].size()-1;
        
        while(top<=down && left<=right){
//             for left to right
            if(dir==0){
                for(int i=left;i<=right;i++){
                    ans.push_back(matrix[top][i]);     
                }
                top++;
            }
//                 for top to down
               else if(dir==1){
                    for(int i=top;i<=down;i++){
                        ans.push_back(matrix[i][right]);
                    }
                    right--;
                }
//                 for right to left
              else  if(dir==2){
                    for(int i=right;i>=left;i--){
                        ans.push_back(matrix[down][i]);
                       
                    } down--;
                }
//             for down to up
           else if(dir==3){
                for(int i=down;i>=top;i--){
                    ans.push_back(matrix[i][left]);
                }
                left++;
            }
            dir=(dir+1)%4;
            
        }
        return ans;
        
        
    }
};