class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd_idx, odd_count = -1, 0
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd_count += 1
                odd_idx = i
        if odd_count > 1:
            return ""

        mid = chr(odd_idx + 97) if odd_idx != -1 else ""
        h = n // 2
        avail = [cnt[i] // 2 for i in range(26)]

        T1 = target[:h]
        target_tail = target[h:]

        def build_full(H: str) -> str:
            return H + mid + H[::-1]

        # Case 1: try H == T1 exactly
        work = avail[:]
        feasible_len = h
        for i, ch in enumerate(T1):
            idx = ord(ch) - 97
            if work[idx] > 0:
                work[idx] -= 1
            else:
                feasible_len = i
                break

        if feasible_len == h:
            candidate_tail = mid + T1[::-1]
            if candidate_tail > target_tail:
                return build_full(T1)

        # Case 2: find rightmost position to place a larger character
        upper = feasible_len if feasible_len < h else h - 1
        for i in range(upper, -1, -1):
            w = avail[:]
            ok = True
            for k in range(i):
                idx = ord(T1[k]) - 97
                if w[idx] <= 0:
                    ok = False
                    break
                w[idx] -= 1
            if not ok:
                continue

            t_idx = ord(T1[i]) - 97
            found = -1
            for c in range(t_idx + 1, 26):
                if w[c] > 0:
                    found = c
                    break
            if found != -1:
                w[found] -= 1
                H = list(T1[:i])
                H.append(chr(found + 97))
                for c in range(26):
                    H.extend([chr(c + 97)] * w[c])
                return build_full("".join(H))

        return ""