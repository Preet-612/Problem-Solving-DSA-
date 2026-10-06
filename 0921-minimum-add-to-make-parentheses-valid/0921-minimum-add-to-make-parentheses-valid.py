class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal=0
        temp=0
        for i in range(len(s)):
            if s[i] == ")":
                if bal==0:
                    temp+=1
                else:
                    bal-=1
            else:
                bal+=1
        return bal+temp

        # stack = []

        # for c in s:
        #     if c == '(':
        #         stack.append(c)
        #     elif stack and stack[-1] == '(':
        #         stack.pop()
        #     else:
        #         stack.append(c)

        # return len(stack)
                

            
        