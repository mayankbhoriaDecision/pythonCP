class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp=[]
        
        for i in range( m):
            
            tmp=[]
            
            for j in range (n):
                
                tmp.append(0)
                
            dp.append(tmp)
            
        i=0
        j=0
            
        
        for i in range(m):
            
            dp[i][0]=1
            
        for j in range(n):
            dp[0][j]=1
            
        
        i=0
        j=0
        
        for i in range(1, m):
            
            for j in range(1,n):
                
                dp[i][j]=dp[i-1][j] + dp[i][j-1]
                
        
        return dp[m-1][n-1]
