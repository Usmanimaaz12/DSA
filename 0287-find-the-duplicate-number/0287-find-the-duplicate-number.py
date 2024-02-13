class Solution:
    #         Taking the nums[1] as index and marking the visited as negative number

    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums :
            i = abs(i)
            if nums[i] < 0 :
                return i
            else :
                nums[i] = -nums[i]
        