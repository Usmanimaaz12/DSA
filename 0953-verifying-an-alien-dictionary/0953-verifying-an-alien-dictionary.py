class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
#         created a map for the given order
        map={}
        for i in range(len(order)):
            map[order[i]]=i
            
#             taking two words at a time and comparing them 
        
        for i in range(1,len(words)):
            first=words[i-1]
            second=words[i]
            
            n=min(len(first),len(second))
            flag=False
            for j in range(n):
#                 if first ka bada then return false 
                if map[first[j]] > map[second[j]]:
                    return False
#         if first ka chhota ho gya then we mark flag true so that we can check if saare letters are same
                elif map[first[j]] < map[second[j]]:
                    flag=True
                    break
                
#             not flag means that saare letters of both words are same 
            if not flag and len(first) > len(second):
                return False
        return True
                