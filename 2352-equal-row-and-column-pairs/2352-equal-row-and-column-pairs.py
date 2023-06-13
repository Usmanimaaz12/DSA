class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        check = collections.defaultdict(int)
        for row in grid:
            s = "-".join(map(str, row))
            check[s] += 1
        
        ans = 0
        for col in range(n):
            arr = []
            for r in range(m):
                arr.append(grid[r][col])
            
            s = "-".join(map(str, arr))
            if s in check:
                ans += check[s]
        
        return ans