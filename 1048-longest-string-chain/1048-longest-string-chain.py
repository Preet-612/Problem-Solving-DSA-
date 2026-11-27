class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        
        def check(s1,s2):
            if len(s1) == len(s2)+1:
                
                i = 0
                j = 0
                while i < len(s1):

                    if j < len(s2) and s1[i] == s2[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            else:
                return False
                
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
        maxi = 1
        for i in range(n):
            for prev in range(i):

                if check(words[i],words[prev]) and dp[i] < dp[prev] + 1:

                    dp[i] = dp[prev]+1
            
            if dp[i] > maxi:
                maxi = dp[i]
        
        return maxi

