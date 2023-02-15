class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        x=int(''.join(list(map(str,num))))
        sm=x+k
        
        return list(map(int,list(str(sm))))
        
        
            
        