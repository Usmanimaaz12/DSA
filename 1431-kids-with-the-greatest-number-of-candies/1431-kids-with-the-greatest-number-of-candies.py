class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        def_max=max(candies)
        ans=[]
        for el in candies:
            if el+extraCandies >= def_max:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        