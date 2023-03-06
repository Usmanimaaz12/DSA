class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
#         implemented using binary search
        if k < arr[0]:
            return k
        low,high=0,len(arr)
        while low<high:
            mid=(low+high)//2
            if arr[mid]-mid-1 < k:
                low=mid+1
            else:
                high=mid
        return low+k
        
        