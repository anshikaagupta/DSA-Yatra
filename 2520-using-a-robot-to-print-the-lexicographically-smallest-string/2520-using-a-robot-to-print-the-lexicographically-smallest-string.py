
class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        stack = []
        result = []
        a_ord = ord('a')

        def has_smaller(top):
            for i in range(top):
                if freq[chr(i + a_ord)] > 0:
                    return True
            return False

        for ch in s:
            freq[ch] -= 1
            stack.append(ch)
            while stack and not has_smaller(ord(stack[-1]) - a_ord):
                result.append(stack.pop())

        return ''.join(result)