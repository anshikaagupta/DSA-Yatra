class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # Step 1: Prepare the conflict list
        conflicts = [[] for _ in range(n + 2)]

        for a, b in conflictingPairs:
            if a < b:
                conflicts[b].append(a)
            else:
                conflicts[a].append(b)
        
        # Step 2: Initialize tracking variables
        max_left = 0
        second_max_left = 0
        gains = [0] * (n + 2)
        valid_subarrays = 0

        # Step 3: Loop through numbers from 1 to n (as subarray end points)
        for right in range(1, n + 1):
            for left in conflicts[right]:
                if left > max_left:
                    second_max_left = max_left
                    max_left = left
                elif left > second_max_left:
                    second_max_left = left
            # Count valid subarrays ending at 'right'
            valid_subarrays += right - max_left
            # Track recoverable subarrays
            gains[max_left] += max_left - second_max_left

        # Step 4: Return total valid subarrays + best recoverable gain
        return valid_subarrays + max(gains)