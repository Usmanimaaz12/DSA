class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=-99999999
        for el in nums:
            currSum+=el
            maxSum=max(currSum,maxSum)
            if currSum<0:
                currSum=0
            
        return maxSum
        