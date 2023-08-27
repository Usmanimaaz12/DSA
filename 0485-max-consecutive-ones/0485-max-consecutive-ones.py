class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = max_count = 0
        for el in nums :
            if el ==1 :
                curr +=1
            else:
                max_count = max(curr, max_count)
                curr = 0
        max_count = max(curr, max_count)
        return max_count