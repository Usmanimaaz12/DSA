class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        # result=[]
        result = set()
#          we can store unique elements in two ways:
# 1. Take set and store the quads in sorted order , sme would be eliminated
# 2. while moving the lptr , rptr, i and j : SKIP THE COMMON ELEMENTS
        for i in range(n):
            for j in range(i+1,n):
                lptr = j+1
                rptr = n-1
                while rptr > lptr :
                    total = nums[i] + nums[j] + nums[lptr] + nums[rptr]
                    if total < target :
                        lptr +=1
                    elif total > target :
                        rptr -= 1
                    else:
                        result.add(tuple(sorted((nums[i],nums[j],nums[lptr],nums[rptr]))))
                        lptr += 1
                        rptr -= 1
        return result
                
        