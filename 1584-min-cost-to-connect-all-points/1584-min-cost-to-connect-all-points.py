class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist=[]
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                dist.append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]),i,j))
#                 here we are using heap to reduce time complexity we could have sorted the array
        heapq.heapify(dist)
        
        par=[i for i in range(n)]
        mstsum=0
        while n>1:
            d,i,j=heapq.heappop(dist)
            pari,parj=par[i],par[j]
            while par[pari] != pari:
                pari=par[pari]
            while par[parj]!=parj:
                parj=par[parj]
            if pari!=parj:
                n-=1
                par[pari]=parj
                mstsum+=d
        return mstsum
        