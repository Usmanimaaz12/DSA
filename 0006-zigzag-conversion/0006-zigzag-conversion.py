class Solution:
    def convert(self, s: str, numRows: int) -> str:
#         I was trying to do using indexing but it tough for me right now 
        # ans=""
        # for i in range(numRows):
        #     ans+=s[i]
        #     j=i+(2*(numRows-i)-2)
        #     while j < len(s):
        #         ans=ans+s[j]
        #         j=j+(2*(numRows-i)-2)
        # return ans
#         i Am using a method in which i will make three lists and traverse up and down 
        if numRows==1:
            return s
        curRow = 0
        rows = [""]*numRows
        
        for ch in s:
           if curRow==0:
                movingDown = True 
           elif curRow==numRows-1:
                movingDown = False
           if movingDown:
            rows[curRow]+=ch
            curRow+=1
           else:
            rows[curRow]+=ch
            curRow-=1
        return "".join(rows)
        
        
            
        
            
        