class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        mp={}
        for el in s:
            if el in mp:
                count+=1
                mp={}
                mp[el]=1
            else:
                mp[el]=1
        return count
                