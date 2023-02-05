class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_P,len_S,P,S,ans=len(p),len(s),0,0,[]
        
        if len_S<len_P:
            return ans
        
        for i in range(len_P):
            P=P+hash(p[i])
            S=S+hash(s[i])
        if P==S:
            ans.append(0)
        
        for i in range(len_P,len_S):
            S= S - hash(s[i-len_P])  + hash(s[i])
           
            if S==P:
                ans.append(i-len_P+1)
        return ans
            