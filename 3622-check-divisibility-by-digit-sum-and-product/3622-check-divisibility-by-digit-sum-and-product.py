class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        for digit in str(n):
            digit_sum += int(digit)
            digit_product *= int(digit)

        return n % (digit_sum + digit_product) == 0