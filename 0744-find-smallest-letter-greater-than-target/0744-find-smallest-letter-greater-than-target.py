class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         Simple BINARY EARCH :
        if target>=letters[-1]:
            return letters[0]
        left,right=0,len(letters)-1
        while left<=right:
            mid=(right+left)//2
            if letters[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        return letters[left] 