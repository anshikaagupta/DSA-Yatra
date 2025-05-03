class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(nums[j])
            result.add(tuple(subset))  # Use tuple to store in set

        return [list(t) for t in result]
