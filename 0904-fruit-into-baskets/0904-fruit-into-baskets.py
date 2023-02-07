class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start,end = 0,0
        max_len=0
        d={}
        #in dict we are storing the indices of the element's last occurence
        
        while end<len(fruits):
            d[fruits[end]] = end
            #when dict length>3 we rea=move the firstly occured fruit bcoz we have only two baskets 
            if len(d)>=3:
                min_ind=min(d.values())
                del d[fruits[min_ind]]
                #we will update start to new start as we need longest sequence 
                start = min_ind+1
            max_len=max(max_len,end-start+1)
            end+=1
        return max_len
        