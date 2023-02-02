class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
#       first find the number of one in each row and in each column
        
        r=len(mat)
        c=len(mat[0])
        
        row=[0 for i in range(r)]
        col=[0 for i in range(c)]
        
        for i in range(r):
            for j in range(c):
                if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1
#      special only if row[i]==1 and col[j]==1 exactly
        count = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    count+=1
                        
        return count