class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        
        first=[]
        second=[]
        
        for el in s1:
            if el not in s2:
                first.append(el)
        
        for el in s2:
            if el not in s1:
                second.append(el)
                
        ans=[]
        ans.append(first)
        ans.append(second)
        return ans