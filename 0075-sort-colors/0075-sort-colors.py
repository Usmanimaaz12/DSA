class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lptr,mid = 0,0
        rptr = len(nums)-1
        while mid<=rptr:
                if nums[mid] == 0:                                       
                    nums[mid],nums[lptr] = nums[lptr],nums[mid]  
                    lptr += 1
                    mid += 1
                elif nums[mid] == 2:
                    nums[mid] , nums[rptr] = nums[rptr],nums[mid]
                    rptr -= 1 
                else :
                    mid += 1
                
        
        