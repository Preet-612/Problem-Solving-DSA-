class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        for r, s in reservedSeats:
            if s in (2, 3, 4, 5, 6, 7, 8, 9):
                rows[r] = rows.get(r, 0) | (1 << s)

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = all(mask & (1 << s) == 0 for s in (2, 3, 4, 5))
            right = all(mask & (1 << s) == 0 for s in (6, 7, 8, 9))

            if left and right:
                ans += 2
            elif left or right:
                ans += 1
            elif all(mask & (1 << s) == 0 for s in (4, 5, 6, 7)):
                ans += 1

        return ans