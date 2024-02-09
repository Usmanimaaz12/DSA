class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         length of nums
        n=len(nums)

        index = -1
# 1         finding breakpoint from right side 
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
#  2     if no breakpoint reverse and return 
        if index == -1 :
            nums.reverse()
            return nums
#   3       if breakpoint : in right half find smallest from right end and swap with index
        for i in range(n-1,index,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index] = nums[index], nums[i]
                break
#    4   reverse the array from the index and return ans
        nums[index+1:] = reversed(nums[index+1:])
        return nums
        
