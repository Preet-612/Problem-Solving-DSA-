class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        ans = []

        for i in range(len(s)):
            c = target[i]

            if freq[c] > 0:
                freq[c] -= 1
                ans.append(c)
            else:
                break
        else:
            i = len(s)

        while True:
            if i < len(s):
                for ch in range(ord(target[i]) + 1, ord('z') + 1):
                    c = chr(ch)
                    if freq[c] > 0:
                        ans.append(c)
                        freq[c] -= 1

                        for x in range(26):
                            ans.extend(chr(ord('a') + x) * freq[chr(ord('a') + x)])

                        return ''.join(ans)

            if not ans:
                return ""

            i -= 1
            last = ans.pop()
            freq[last] += 1