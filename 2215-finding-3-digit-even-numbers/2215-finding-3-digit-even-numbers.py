class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        res = []
        for num in range(100, 999, 2):
            h = num // 100
            t = (num // 10) % 10
            o = num % 10
            if count[h]:
                count[h] -= 1
                if count[t]:
                    count[t] -= 1
                    if count[o]:
                        res.append(num)
                    count[t] += 1
                count[h] += 1
        return res