class Solution:
    def maxDepth(self, s: str) -> int:
        temp=0
        ans=0
        for i in s:
            if i =='(':
                temp+=1
                ans=max(temp,ans)
            elif i ==')':
                temp-=1
            else:
                continue
    
        return ans