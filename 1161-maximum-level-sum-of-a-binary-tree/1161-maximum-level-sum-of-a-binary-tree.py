class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         Applying simple BREADTH-FIRST-SEARCH
        q = [root]
        maxi = -maxsize
        ans = 1
        cnt = 1
        while q:
            t = q.copy()
            q.clear()
            s = 0
            for node in t:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                s += node.val
            if s > maxi:
                maxi = s
                ans = cnt
            cnt += 1
        return ans