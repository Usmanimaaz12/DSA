class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(dict)
        #defaultdict never raises keyerror it returns default value in its bracket , here "dict"
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        min_score = float('inf')
#         inf returns floating point positive infinity
        visited = set()
        queue = deque([1])

        while queue:
            node = queue.popleft()
            for adj, score in graph[node].items():
                if adj not in visited:
                    queue.append(adj)
                    visited.add(adj)
                min_score = min(min_score, score)
                
        return min_score