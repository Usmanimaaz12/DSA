class Solution:
#     We will consider the 2D matrix as 1D array.
#  calculation of index considering it as 1D array:
#       row = index / no. of cols
#       col = index % no. of cols
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =len(matrix)
        col = len(matrix[0])
        low,high = 0 , len(matrix)*len(matrix[0])-1
        
        while low <= high:
            mid =  low + (high - low)//2
            if matrix[mid//col][mid%col] == target :
                return True
            elif matrix[mid//col][mid%col] > target :
                high = mid -1
            else :
                low = mid+1
        return False
        
        