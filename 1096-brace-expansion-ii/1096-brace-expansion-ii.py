class Solution:
    def braceExpansionII(self, expression: str):
        n = len(expression)
        i = 0

        # Handles union: e1,e2,e3
        def parse_expression():
            nonlocal i

            result = parse_concat()

            while i < n and expression[i] == ',':
                i += 1
                result |= parse_concat()

            return result

        # Handles concatenation: e1e2e3
        def parse_concat():
            nonlocal i

            result = {""}

            while i < n and expression[i] not in "},":
                current = parse_term()

                result = {
                    a + b
                    for a in result
                    for b in current
                }

            return result

        # Handles a single letter or {...}
        def parse_term():
            nonlocal i

            if expression[i].islower():
                ch = expression[i]
                i += 1
                return {ch}

            # expression[i] == '{'
            i += 1  # skip '{'

            result = parse_expression()

            i += 1  # skip '}'

            return result

        return sorted(parse_expression())