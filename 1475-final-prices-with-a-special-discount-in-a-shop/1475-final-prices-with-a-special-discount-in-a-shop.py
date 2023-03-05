class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st=[]
        for i in range(len(prices)-1,-1,-1):
            el= prices[i]
            while st and st[-1]>el:
                st.pop()
            if st:
                prices[i]=el-st[-1]
            st.append(el)
        return prices
        