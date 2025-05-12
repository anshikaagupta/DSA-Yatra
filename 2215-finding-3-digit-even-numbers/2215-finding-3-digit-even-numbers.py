class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d = defaultdict(int)
        res = []

        for num in digits:
            d[str(num)] += 1

        for i in range(100, 999, 2):
            new_d = {}

            for j in (str(i)):
                new_d[j] = new_d.get(j, 0) + 1

                if new_d[j] > d[j]:
                    break
            else:
                res.append(i)

        return res