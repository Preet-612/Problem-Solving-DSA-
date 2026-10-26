class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        sum = 0
        for i in nums:
            sum += i
        
        if sum % 2 != 0:
            return False
            
        n = len(nums)
        target = sum // 2
        dp = [[False]*(target+1) for i in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]]
        
        for idx in range(1,n):
            for t in range(target+1):
                notTake = dp[idx-1][t]
                take = False
                if nums[idx] <= t:
                    take = dp[idx-1][t-nums[idx]]
                
                dp[idx][t] = take or notTake
        
        return dp[n-1][target]

        # def helper(idx,tar):

        #     if tar == 0:
        #         return True

        #     if idx == 0:
        #         return False

        #     if dp[idx][tar] != -1:
        #         return dp[idx][tar]

        #     take = helper(idx-1,tar - nums[idx])
        #     notTake = helper(idx-1,tar)

        #     dp[idx][tar] = take or notTake
        #     return dp[idx][tar]
        
        # return helper(n-1,target)
            
