class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        m={}
        for i in range(len(s)):
                m[s[i]]=i
        stack=[]
#         with set we can search or check in O(1) time
        present=set()
        for i,el in enumerate(s):
            if el in present:
                continue
            while stack and stack[-1]> el and m[stack[-1]]>i:
                t = stack.pop()
                present.remove(t)
            stack.append(el)
            present.add(el)
        return "".join(stack)
                
            