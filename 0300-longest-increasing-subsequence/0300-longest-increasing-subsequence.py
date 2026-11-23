class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            temp = [0]*(n+1)
            for prev in range(i-1,-2,-1):
                ntk = dp[prev]
                tk = 0
                if prev == -1 or nums[prev] < nums[i]:
                    tk = 1 + dp[i]
                temp[prev] = max(ntk,tk)
            dp = temp
        
        return dp[-1]

        # dp = [[0]*(n+1) for i in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for prev in range(i-1,-2,-1):
        #         ntk = dp[i+1][prev]
        #         tk = 0
        #         if prev == -1 or nums[prev] < nums[i]:
        #             tk = 1 + dp[i+1][i]
        #         dp[i][prev] = max(ntk,tk)
        
        # return dp[0][-1]

        # def helper(i,prev):

        #     if i == n:
        #         return 0
            
        #     if dp[i][prev] != -1:
        #         return dp[i][prev]

        #     ntk = helper(i+1,prev)
        #     tk = 0
        #     if prev == -1 or nums[prev] < nums[i]:
        #         tk = 1 + helper(i+1,i)
        #     dp[i][prev] = max(ntk,tk)
        #     return dp[i][prev]

        # return helper(0,-1)