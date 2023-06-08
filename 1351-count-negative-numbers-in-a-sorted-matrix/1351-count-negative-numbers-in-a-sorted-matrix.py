class Solution:
#     BINARY SEARCH for finding the starting of the negative values
    def search_neg(self, row, n):
        start, end = 0, n-1
        while start<=end:
            mid = (start+end)//2
            if row[mid] >= 0:
                start = mid+1
            else:
                end = mid - 1
        return n-start    
    
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        row, col = len(grid), len(grid[0])
#         for each row we are counting the negative values
        for i in range(row):
            c+=self.search_neg(grid[i],col)
        return c