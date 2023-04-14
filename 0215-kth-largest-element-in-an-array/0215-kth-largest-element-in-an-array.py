class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp=[]
        for el in nums:
#             min heap ok k element is maintained : k-1 elements greater than root of heap is always maintained ...in the end we return the top element.
            if len(hp)<k:
                heapq.heappush(hp,el)
            else:
                if el>hp[0]:
                    heapq.heappop(hp)
                    heapq.heappush(hp,el)
        return hp[0]
        