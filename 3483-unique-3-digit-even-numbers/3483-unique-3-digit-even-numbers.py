class Solution:
    def totalNumbers(self, digits):
        count = 0

        # Count frequency of each digit
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        # Try every 3-digit number
        for num in range(100, 1000):

            # Number must be even
            if num % 2 != 0:
                continue

            # Extract digits
            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check if digits are available
            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            valid = True

            for d in range(10):
                if used[d] > freq[d]:
                    valid = False
                    break

            if valid:
                count += 1

        return count