class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_or=0
        rott_q=deque()
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh_or+=1
                if grid[i][j]==2:
                    rott_q.appendleft((i,j,0))
        if not fresh_or:
            return 0
        directions={(0,1),(0,-1),(-1,0),(1,0)}
        while rott_q:
            pre_i,pre_j,time=rott_q.pop()
#             for loop is performing BFS
            for di,dj in directions:
                new_i,new_j=pre_i+di,pre_j+dj
                if -1<new_i<m and -1<new_j<n and grid[new_i][new_j]==1:
                    fresh_or-=1
                    if fresh_or==0:
                        return time+1
                    grid[new_i][new_j]=2
                    rott_q.appendleft((new_i,new_j,time+1))
        if not rott_q:
            return -1
            
            
        