class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
#         memoizing by making 2D list [[],[],[]]
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        
        def helper(i,j,n,m):
            if i == n-1 and  j == m-1 :
                return 1
            if i >= n or j>= m :
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            else :
#                 left and right recursive call 
                dp[i][j]=helper(i+1,j,n,m) + helper(i,j+1,n,m)
                return dp[i][j]
        return helper(0,0,m,n)