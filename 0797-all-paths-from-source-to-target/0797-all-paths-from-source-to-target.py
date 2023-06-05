class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def paths(curr_path):
            if n-1==curr_path[-1]:
                ans.append(curr_path[:])
                return
            for el in graph[curr_path[-1]]:
                curr_path.append(el)
                paths(curr_path)
                curr_path.pop()
        paths([0])
        return ans
        