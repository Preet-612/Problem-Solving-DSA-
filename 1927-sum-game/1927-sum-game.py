class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left_sum = right_sum = 0
        left_q = right_q = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < n // 2:
                    left_q += 1
                else:
                    right_q += 1
            else:
                if i < n // 2:
                    left_sum += int(ch)
                else:
                    right_sum += int(ch)

        total_q = left_q + right_q

        if total_q % 2:
            return True

        return left_sum - right_sum != (right_q - left_q) * 9 // 2