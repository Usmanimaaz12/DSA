class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr=0
        set_v={'a','e','i','o','u'}
       
        for i in range(k):
            if s[i] in set_v:
                curr+=1
        overall_max=curr
        
        for i in range(k,len(s)):
            if s[i-k] in set_v:
                curr-=1
            if s[i] in set_v:
                curr+=1
            if curr>overall_max:
                overall_max=curr
        return overall_max
        