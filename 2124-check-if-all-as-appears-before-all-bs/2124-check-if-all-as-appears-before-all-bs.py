class Solution:
    def checkString(self, s: str) -> bool:
        temp=0
        for i in range(0,len(s)):
            if s[i]=='b':
                temp=1;
                continue;
            if s[i]=='a' and temp==1:
                return False
        return True