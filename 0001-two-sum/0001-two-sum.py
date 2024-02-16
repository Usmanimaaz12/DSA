class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index,el in enumerate(nums):
            if el in dict :
                return dict[el] , index
            else :
                dict[target-el] = index
        