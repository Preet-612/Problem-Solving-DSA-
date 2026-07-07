class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        num = str(n)
        s = 0
        st = ""
        for i in num:
            if int(i) != 0:
                s += int(i)
                st += str(i)

        return s * int(st) if len(num) > 1 or int(num[0]) != 0 else s     