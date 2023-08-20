class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)-1):
            # print(nums[i],nums[i+1])
            if nums[i]>nums[i+1]:
                count +=1
                # print(count)
        if nums[len(nums)-1] > nums[0]:
            count+=1
        # print(count)
        return count<=1