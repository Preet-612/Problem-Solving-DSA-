class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        sq = [0] * (4 * n)

        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return

            if ql <= l and r <= qr:
                sq[node] = (sq[node] + 2 * val * tree[node] + (r - l + 1) * val * val) % MOD
                tree[node] = (tree[node] + (r - l + 1) * val) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return

            mid = (l + r) // 2
            push(node, l, r)

            update(node * 2, l, mid, ql, qr, val)
            update(node * 2 + 1, mid + 1, r, ql, qr, val)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2
            for child, a, b in (
                (node * 2, l, mid),
                (node * 2 + 1, mid + 1, r)
            ):
                val = lazy[node]
                length = b - a + 1
                sq[child] = (
                    sq[child] + 2 * val * tree[child] + length * val * val
                ) % MOD
                tree[child] = (tree[child] + length * val) % MOD
                lazy[child] = (lazy[child] + val) % MOD

            lazy[node] = 0

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            start = last.get(x, -1) + 1
            update(1, 0, n - 1, start, i, 1)
            last[x] = i
            ans = (ans + sq[1]) % MOD

        return ans