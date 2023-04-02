class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return self.helper(spells,potions,success)
    def helper(self,arr1,arr2,success):
        n2=len(arr2)
        arr2.sort()
        ans=[]
        for i in arr1:
            val=math.ceil(success/i)
            idx=bisect.bisect_left(arr2,val)
            res=n2-idx
            ans.append(res)
        return ans
        