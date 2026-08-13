class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        size = 4 * n

        lc = [''] * size
        rc = [''] * size
        left = [0] * size
        right = [0] * size
        best = [0] * size
        length = [0] * size

        def pull(node):
            l = node * 2
            r = l + 1

            lc[node] = lc[l]
            rc[node] = rc[r]
            length[node] = length[l] + length[r]

            left[node] = left[l]
            if left[l] == length[l] and rc[l] == lc[r]:
                left[node] += left[r]

            right[node] = right[r]
            if right[r] == length[r] and rc[l] == lc[r]:
                right[node] += right[l]

            best[node] = max(best[l], best[r])

            if rc[l] == lc[r]:
                best[node] = max(best[node], right[l] + left[r])

        def build(node, lo, hi):
            if lo == hi:
                lc[node] = rc[node] = s[lo]
                left[node] = right[node] = best[node] = 1
                length[node] = 1
                return

            mid = (lo + hi) // 2
            build(node * 2, lo, mid)
            build(node * 2 + 1, mid + 1, hi)
            pull(node)

        def update(node, lo, hi, idx, ch):
            if lo == hi:
                lc[node] = rc[node] = ch
                return

            mid = (lo + hi) // 2

            if idx <= mid:
                update(node * 2, lo, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, hi, idx, ch)

            pull(node)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(best[1])

        return ans