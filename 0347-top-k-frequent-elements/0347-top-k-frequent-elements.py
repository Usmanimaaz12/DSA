
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         usig Heaps
        freq= Counter(nums)
        print(freq)
        hp=[]
        for el in freq:
            count = freq[el]
            heapq.heappush(hp,(count,el))
            if len(hp)>k:
                heapq.heappop(hp)
        return [x[1] for x in hp]
        