class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j=1,n
        
        while j< 2*n:
            nums.insert(i,nums.pop(j))
            i+=2
            j+=1
        return nums