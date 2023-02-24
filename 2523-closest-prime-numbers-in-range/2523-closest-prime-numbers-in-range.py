class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        # Sieve Of Eratosthenes method to generate prime no  
      
        seieve=[0]*(right+1)
        seieve[1]=1
        seieve[0]=1

        for i in range(2,right+1):
            if seieve[i]==0:
                j=i*i
                while(j<=right):
                    seieve[j]=1
                    j+=i

        # list of all prime numbers in a given range (left,right)

        prime=[]

        for i in range(left,right+1):
            if seieve[i]==0:
                prime.append(i) 


        # finding min difference pair 

        if len(prime)>=2:
            
            mi=9999999
            for i in range(0,len(prime)-1):
                s=prime[i+1]-prime[i]

                if s<mi:
                    mi=s
                    result=[prime[i],prime[i+1]]
            return result
        else:
            return [-1,-1]

