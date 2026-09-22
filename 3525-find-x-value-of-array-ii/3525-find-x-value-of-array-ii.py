class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # Segment tree size
        size = 1
        while size < n:
            size *= 2

        # Each node:
        # [product_of_whole_segment, prefix_count]
        #
        # prefix_count[r] =
        # number of non-empty prefixes whose product % k == r

        tree = [None] * (2 * size)

        # Empty segment
        # Product of empty segment = 1
        identity = (1 % k, [0] * k)

        # Create leaf
        def make_leaf(value):
            r = value % k

            prefix = [0] * k
            prefix[r] = 1

            return (r, prefix)

        # Merge two consecutive segments:
        #
        # A + B
        #
        # Prefixes of A+B are:
        #
        # 1. prefixes completely inside A
        # 2. entire A + a prefix of B
        #
        def merge(A, B):

            prodA, prefA = A
            prodB, prefB = B

            # Product of entire combined segment
            prod = (prodA * prodB) % k

            # Start with prefixes completely inside A
            pref = prefA[:]

            # Entire A + prefix of B
            #
            # product = prodA * prefix_product
            for r in range(k):
                if prefB[r] > 0:
                    new_remainder = (prodA * r) % k
                    pref[new_remainder] += prefB[r]

            return (prod, pref)

        # -------------------------
        # Build tree
        # -------------------------

        for i in range(n):
            tree[size + i] = make_leaf(nums[i])

        # Remaining leaves are empty
        for i in range(n, size):
            tree[size + i] = identity

        # Build bottom-up
        for i in range(size - 1, 0, -1):
            tree[i] = merge(
                tree[2 * i],
                tree[2 * i + 1]
            )

        # -------------------------
        # Point update
        # -------------------------

        def update(index, value):

            pos = size + index

            tree[pos] = make_leaf(value)

            pos //= 2

            while pos:

                tree[pos] = merge(
                    tree[2 * pos],
                    tree[2 * pos + 1]
                )

                pos //= 2

        # -------------------------
        # Range query [left, right)
        # -------------------------

        def query(left, right):

            left += size
            right += size

            left_result = None
            right_result = None

            while left < right:

                if left & 1:

                    if left_result is None:
                        left_result = tree[left]
                    else:
                        left_result = merge(
                            left_result,
                            tree[left]
                        )

                    left += 1

                if right & 1:

                    right -= 1

                    if right_result is None:
                        right_result = tree[right]
                    else:
                        right_result = merge(
                            tree[right],
                            right_result
                        )

                left //= 2
                right //= 2

            # Only one side exists
            if left_result is None:
                return right_result

            if right_result is None:
                return left_result

            # IMPORTANT:
            # preserve left-to-right order
            return merge(
                left_result,
                right_result
            )

        # -------------------------
        # Process queries
        # -------------------------

        answer = []

        for index, value, start, x in queries:

            # Update persists for all future queries
            update(index, value)

            # Remaining array:
            #
            # nums[start ... n-1]
            #
            # We need number of prefixes
            # having product % k == x.
            node = query(start, n)

            product, prefix_count = node

            answer.append(prefix_count[x])

        return answer