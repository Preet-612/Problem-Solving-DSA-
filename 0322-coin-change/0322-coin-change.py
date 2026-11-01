class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        n = len(coins)
        if n == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1
        dp = [[-1]*(amount+1) for i in range(n)]
        def helper(idx,tar):

            if idx == 0:
                if tar % coins[0] == 0:
                    return tar // coins[0]
                else:
                    return float('inf')
            if dp[idx][tar] != -1:
                return dp[idx][tar]
            notPick = 0 + helper(idx-1,tar)
            pick = float('inf')
            if coins[idx] <= tar:
                pick = 1 + helper(idx,tar-coins[idx])
            
            dp[idx][tar] = min(pick,notPick)
            return dp[idx][tar]

        ans = helper(n-1,amount) 
        if ans == float('inf'):
            return -1
        return ans
         
