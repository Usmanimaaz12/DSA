class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min=999999999
        max_so_far=0
        for i in prices:
            if i < curr_min:
                curr_min=i
            max_so_far=max(max_so_far,i-curr_min)
        return max_so_far
        