class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i=="*":
                stack.pop()
            else:
                stack.append(i)
        return  "".join(stack)
    
    
#     What i wrote at first
    #         ans=""
    #         for i in s:
    #             if i== "*":
    #                 if stack:
    #                     stack.pop()
    #             else:
    #                 stack.append(i)
    #         while stack:
    #             ans=stack[-1]+ans
    #             stack.pop()
    #         return ans