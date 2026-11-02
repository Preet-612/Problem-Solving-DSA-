class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        if total - target < 0 or (total + target) % 2 != 0:
            return 0
        
        newT = (total-target)//2

        dp = [0]*(newT+1)

        if nums[0] == 0:
            dp[0] = 2
        else:
            dp[0] = 1
        
        if nums[0] != 0 and nums[0] <= newT:
            dp[nums[0]] = 1

        for idx in range(1,n):
            temp = [0]*(newT+1)
            for tar in range(newT+1):
                add = dp[tar]
                sub = 0
                if nums[idx] <= tar:
                    sub = dp[tar-nums[idx]]
                
                temp[tar] = add + sub
            dp = temp
        return dp[newT]



        # def helper(idx,tar):
            
        #     if idx == 0:
        #         if tar == 0 and nums[0] == 0:
        #             return 2
        #         if tar == 0 or nums[0] == tar:
        #             return 1
        #         return 0
            
        #     add = helper(idx-1,tar)
        #     sub = 0
        #     if nums[idx] <= tar:
        #         sub = helper(idx-1,tar-nums[idx])

        #     return add + sub
        
        # return helper(n-1,newT)