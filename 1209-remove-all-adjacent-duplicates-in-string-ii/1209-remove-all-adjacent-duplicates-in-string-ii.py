class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # a=[]
        # for i in s:
        #     if a and a[-1][0]==i:
        #         a[-1][1]+=1
        #         if a[-1][1]==k: a.pop()
        #     else: a.append([i,1])
        # return ''.join(key*value for key, value in a)      
        stack=[]
        for el in s:
            if stack and stack[-1][0]==el:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else :
                stack.append([el,1])
        return "".join(key*values for key,values in stack)
                
            
        