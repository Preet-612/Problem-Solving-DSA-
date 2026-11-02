class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        
        n = len(coins)
        dp = [[-1]*(amount+1) for i in range(n)]
        def helper(idx,tar):
            if tar == 0:
                return 1
            if idx == 0:
                if tar % coins[0] == 0:
                    return 1
                else:
                    return 0
                
            if dp[idx][tar] != -1:
                return dp[idx][tar]
            p = 0
            if coins[idx] <= tar:
                p = helper(idx,tar-coins[idx])
            np = helper(idx-1,tar)

            dp[idx][tar] = p + np
            return dp[idx][tar]
        
        ans = helper(n-1,amount)
        if ans != float('inf'):
            return ans
        return 0
            
