class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def is_valid_diff(x):
            last, count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= x:
                    last, count = price[i], count + 1
                i += 1
            return count == k
       
        max_diff=price[-1]-price[0]
        if max_diff==0:
            return 0
        
        low=0
        high=max(price)-min(price)
        ans=-1
        
        while low<=high:
            mid=(low+high)//2
            if is_valid_diff(mid)==True:
                low=mid+1
                ans=mid
            else:
                high=mid-1
        
        return ans
                
        
        
        