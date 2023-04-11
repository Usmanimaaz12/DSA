class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        ans=""
        for i in s:
            if i== "*":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        while stack:
            ans=stack[-1]+ans
            stack.pop()
        return ans
            