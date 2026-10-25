class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        sum = 0
        for i in nums:
            sum += i
        
        if sum % 2 != 0:
            return False
            
        n = len(nums)
        target = sum // 2
        dp = [[-1]*(target+1) for i in range(n)]
        def helper(idx,tar):

            if tar == 0:
                return True

            if idx == 0:
                return False

            if dp[idx][tar] != -1:
                return dp[idx][tar]

            take = helper(idx-1,tar - nums[idx])
            notTake = helper(idx-1,tar)

            dp[idx][tar] = take or notTake
            return dp[idx][tar]
        
        return helper(n-1,target)
            
