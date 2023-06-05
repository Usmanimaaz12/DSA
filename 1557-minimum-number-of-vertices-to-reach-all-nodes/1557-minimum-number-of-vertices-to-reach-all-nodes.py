class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_edge=[x[1] for x in edges]
        in_edge_set=set(in_edge)
        ans=[]
        n=1+max([x[0] for x in edges]+[x[1] for x in edges])
        for i in range(n):
            if i not in in_edge_set:
                ans.append(i)
        return ans
        