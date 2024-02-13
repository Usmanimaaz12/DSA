class Solution:
            
#         Two CASES:
#           If the new interval cannot be merged then push it into the ans
#           If it can be merged : Then high would be the max of the curr_high and the arr wala
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         Firstly we would sort the intervals
        intervals.sort()
        ans = []
        
        n= len(intervals)
        
        for i in range(n):
#             If intervals cannot be merged
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
#                 If intervals can be merged
            else:
                ans[-1][1]= max(intervals[i][1], ans[-1][1])
        return ans
        

    