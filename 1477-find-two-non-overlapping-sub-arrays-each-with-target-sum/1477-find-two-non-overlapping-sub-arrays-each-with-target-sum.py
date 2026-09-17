class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = shortest valid subarray ending at or before i
        best = [float('inf')] * n

        left = 0
        curr_sum = 0
        ans = float('inf')
        min_len = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum becomes too large
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray with sum == target
            if curr_sum == target:
                length = right - left + 1

                # Combine with a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            # Best valid subarray seen so far
            best[right] = min_len

        return -1 if ans == float('inf') else ans