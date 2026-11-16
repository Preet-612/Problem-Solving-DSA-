class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        
        n = len(s1)
        s2 = s1[::-1]
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            temp = [0]*(n+1)
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]: 
                    temp[j] =  1 + dp[j-1]
                else:
                    temp[j] =  max(dp[j],temp[j-1])
            
            dp = temp
        
        return dp[n]

        # def helper(i,j):

        #     if i < 0 or j < 0:
        #         return 0
        #     # p = 0
        #     if s1[i] == s2[j]: 
        #         return 1 + helper(i-1,j-1)
        #     return  max(helper(i-1,j),helper(i,j-1))
        
        # return helper(n-1,n-1)
        