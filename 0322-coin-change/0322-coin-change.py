class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        n = len(coins)
        if n == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1

        
        dp = [[float('inf')]*(amount+1) for i in range(n)]

        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            

        for idx in range(1,n):
            for tar in range(amount+1):

                notPick = 0 + dp[idx-1][tar]
                pick = float('inf')
                if coins[idx] <= tar:
                    pick = 1 + dp[idx][tar-coins[idx]]
                
                dp[idx][tar] = min(pick,notPick)

        if dp[n-1][amount] != float('inf'):
            return dp[n-1][amount]
        else:
            return -1

        # def helper(idx,tar):

        #     if idx == 0:
        #         if tar % coins[0] == 0:
        #             return tar // coins[0]
        #         else:
        #             return float('inf')
        #     if dp[idx][tar] != -1:
        #         return dp[idx][tar]
        #     notPick = 0 + helper(idx-1,tar)
        #     pick = float('inf')
        #     if coins[idx] <= tar:
        #         pick = 1 + helper(idx,tar-coins[idx])
            
        #     dp[idx][tar] = min(pick,notPick)
        #     return dp[idx][tar]

        # ans = helper(n-1,amount) 
        # if ans == float('inf'):
        #     return -1
        # return ans
         
