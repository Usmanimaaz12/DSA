class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2 
            
			#Case 1
            if nums[mid] == target:
                return mid
            
			#Case 2
            if nums[mid] < target:
                left = mid + 1
            
			#Case 3
            if nums[mid] > target:
                right = mid - 1 
				
        #if the element is not present in the array
		#the condition inside the while loop will fail and we will return -1
        return -1
        