
import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:

        n = len(nums)

        left = []
        right = []

        sum_left = 0
        sum_right = 0

        delayed = defaultdict(int)
        left_size = 0
        right_size = 0

        def prune(heap, is_left):
            while heap:
                val = -heap[0] if is_left else heap[0]

                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():

            nonlocal left_size, right_size
            nonlocal sum_left, sum_right

            prune(left, True)
            prune(right, False)

            while left_size > right_size + 1:

                val = -heapq.heappop(left)

                left_size -= 1
                right_size += 1

                sum_left -= val
                sum_right += val

                heapq.heappush(right, val)

                prune(left, True)

            while left_size < right_size:

                val = heapq.heappop(right)

                right_size -= 1
                left_size += 1

                sum_right -= val
                sum_left += val

                heapq.heappush(left, -val)

                prune(right, False)

        def add(val):

            nonlocal left_size, right_size
            nonlocal sum_left, sum_right

            prune(left, True)

            if not left or val <= -left[0]:

                heapq.heappush(left, -val)
                left_size += 1
                sum_left += val

            else:

                heapq.heappush(right, val)
                right_size += 1
                sum_right += val

            rebalance()

        def remove(val):

            nonlocal left_size, right_size
            nonlocal sum_left, sum_right

            delayed[val] += 1

            if val <= -left[0]:

                left_size -= 1
                sum_left -= val

                if val == -left[0]:
                    prune(left, True)

            else:

                right_size -= 1
                sum_right -= val

                if right and val == right[0]:
                    prune(right, False)

            rebalance()

        def get_cost():

            prune(left, True)

            median = -left[0]

            return (
                median * left_size - sum_left
                + sum_right - median * right_size
            )

        costs = []

        for i in range(n):

            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        inf = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):

            curr = [inf] * (n + 1)

            for i in range(1, n + 1):

                curr[i] = curr[i - 1]

                if i >= x and prev[i - x] != inf:

                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
