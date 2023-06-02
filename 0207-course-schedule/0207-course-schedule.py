class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=[[0,set()] for i in range(numCourses)]
#         TOPOLOGICAL SORT
        for req in prerequisites:
            dst,src=req
            g[dst][0]+=1
            g[src][1].add(dst)
            
        q=deque([x for x in range(numCourses) if g[x][0]==0])
        c=numCourses
        while q:
            c-=1
            el=q.popleft()
            for adjel in g[el][1]:
                g[adjel][0]-=1
                if g[adjel][0] == 0:
                    q.append(adjel)
        return 1 if c==0 else 0