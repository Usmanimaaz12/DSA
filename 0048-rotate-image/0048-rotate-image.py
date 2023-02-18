class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            row.reverse()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m-1):
            for j in range(m-i-1):
                matrix[i][j],matrix[m-j-1][n-i-1]=matrix[m-j-1][n-i-1],matrix[i][j]
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        