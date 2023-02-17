#User function Template for python3
class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        sum=0
        for i in range(K):
            sum+=GeekNum[i]
        for i in range(K,N):
            GeekNum.append(sum)
            sum=sum*2-GeekNum[i-K]
            
            
        return GeekNum[N-1]

            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
    
# } Driver Code Ends