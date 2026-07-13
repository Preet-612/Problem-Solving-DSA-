class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"
        ans = []

        min_len = len(str(low))
        max_len = len(str(high))

        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                num = int(nums[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans