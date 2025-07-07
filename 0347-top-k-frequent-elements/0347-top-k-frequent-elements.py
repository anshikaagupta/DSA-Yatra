class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        ans_table = freq_table.most_common()
        ans = []
        for key, _ in ans_table:
            if k <= 0:
                break
            k -= 1
            ans.append(key)
        return ans