class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis= set()
        n=len(isConnected)
        count=0
        for i in range(n):
            if i in vis:
                continue
            count+=1
            vis.add(i)
            q=deque([i])
            while q:
                el=q.pop()
                for adj_el in range(n):
                    if isConnected[el][adj_el] and adj_el not in vis:
                        vis.add(adj_el)
                        q.appendleft(adj_el)
        return count
            
        