from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval that does NOT overlap i
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        # dp[i][k] = best (score, indices) from i onward
        #
        # We process from right to left.
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            """
            Return the better of two states.
            First maximize score.
            If scores equal, choose lexicographically smaller indices.
            """
            score_a, ids_a = a
            score_b, ids_b = b

            if score_a != score_b:
                return a if score_a > score_b else b

            return a if ids_a < ids_b else b

        for i in range(n - 1, -1, -1):

            for k in range(1, 5):

                # Option 1: don't choose this interval
                skip = dp[i + 1][k]

                # Option 2: choose this interval
                next_i = nxt[i]

                next_score, next_ids = dp[next_i][k - 1]

                take_score = arr[i][2] + next_score
                take_ids = next_ids + [arr[i][3]]

                # Sort indices because answer must be lexicographically
                # compared by original indices.
                take_ids.sort()

                take = (take_score, take_ids)

                dp[i][k] = better(skip, take)

        return dp[0][4][1]