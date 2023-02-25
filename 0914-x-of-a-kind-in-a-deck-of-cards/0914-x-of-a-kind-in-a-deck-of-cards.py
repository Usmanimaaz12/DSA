class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            if (b == 0):
                return a
            return gcd(b, a%b)
        mp={}
        for num in deck:
            if num not in mp:
                mp[num]=1
            else:
                mp[num]+=1
#                 finding hcf of frequencies
        min_val=mp[deck[0]]
        for value in mp.values():
            min_val=gcd(max(min_val,value),min((min_val,value)))
        print(min_val)
        return min_val>1
            