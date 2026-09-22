class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')

            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Find the smallest valid interval
        # starting at first occurrence of each character.
        for c in range(26):

            if first[c] == n:
                continue

            start = first[c]
            end = last[c]

            i = start
            valid = True

            while i <= end:

                curr = ord(s[i]) - ord('a')

                # Character occurs before start,
                # so we cannot create a valid substring
                # starting here.
                if first[curr] < start:
                    valid = False
                    break

                # We must include all occurrences
                # of this character.
                end = max(end, last[curr])

                i += 1

            if valid:
                intervals.append((start, end))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []

        prev_end = -1

        for start, end in intervals:

            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result