class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Step 1: Ensure nums1 is the smaller array to optimize performance
        if len(nums1) > len(nums2):
            return self.kthSmallestProduct(nums2, nums1, k)

        # Step 2: Define the binary search range for possible product values
        lo, hi = -10**10, 10**10  # large enough to cover all product cases

        # Step 3: Perform binary search to find the kth smallest product
        while lo < hi:
            mid = (lo + hi) // 2

            # Step 4: Count number of products <= mid using helper function
            count = self.countLE(mid, nums1, nums2)

            # Step 5: Adjust search bounds based on count
            if count < k:
                lo = mid + 1  # we need a larger product
            else:
                hi = mid      # try a smaller or same product

        # Step 6: Return the kth smallest product
        return lo

    def countLE(self, x: int, A: List[int], B: List[int]) -> int:
        # Step 1: Initialize counter
        count = 0
        n = len(B)

        # Step 2: Handle the case when x >= 0
        if x >= 0:
            jPos = n - 1
            jNeg = n - 1

            for a in A:
                if a > 0:
                    # Count B[j] such that a * B[j] <= x
                    while jPos >= 0 and a * B[jPos] > x:
                        jPos -= 1
                    count += jPos + 1
                elif a == 0:
                    # All products with 0 are 0 <= x
                    count += n
                else:
                    # a < 0 and x >= 0
                    while jNeg >= 0 and a * B[jNeg] <= x:
                        jNeg -= 1
                    count += n - 1 - jNeg

        # Step 3: Handle the case when x < 0
        else:
            jPos = 0
            jNeg = 0

            for a in A:
                if a > 0:
                    while jPos < n and a * B[jPos] <= x:
                        jPos += 1
                    count += jPos
                elif a == 0:
                    # 0 * B[j] > x (since x is negative), so count += 0
                    continue
                else:
                    while jNeg < n and a * B[jNeg] > x:
                        jNeg += 1
                    count += n - jNeg

        # Step 4: Return total number of products <= x
        return count