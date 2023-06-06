class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
#         check if the difference between all the elements is same (if same then len(set)==1)
        return len(set(arr[i-1] - arr[i] for i in range(1, len(arr)))) == 1