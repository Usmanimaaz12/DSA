class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par= [x for x in range(1001)]
#         UNION FIND ALGORITHM
        for edge in edges:
            node_a,node_b=edge
            par_a,par_b=node_a,node_b
            
            while par_a != par[par_a]:
                par_a = par[par_a]
            while par_b != par[par_b]:
                par_b = par[par_b]
            if par_a != par_b:
                par[par_a] = par_b
            else:
                return edge