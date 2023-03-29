class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        v=sorted(satisfaction,reverse=True)
        sum=0
        ans=0
#         prefix sum 
        for i in v:
            if(sum+i>0):
                ans+=sum+i
                sum+=i
            else:
                break
        return ans  