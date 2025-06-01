class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        from math import comb
        def count_ways(x):
            if x < 0:
                return 0
            return comb(x + 2, 2)
    
        total = count_ways(n)
        # Subtract cases where at least one child exceeds limit
        total -= 3 * count_ways(n - (limit + 1))
        # Add back cases where two children exceed limit (double subtracted)
        total += 3 * count_ways(n - 2 * (limit + 1))
        # Subtract cases where all three exceed limit
        total -= count_ways(n - 3 * (limit + 1))
        return total