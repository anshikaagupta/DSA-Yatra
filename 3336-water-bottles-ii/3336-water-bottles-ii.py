class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        eb, x, ans = numBottles, numExchange, numBottles
        while eb >= x:
            eb -= x
            eb += 1
            ans += 1
            x += 1
        return ans