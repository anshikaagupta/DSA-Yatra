class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        # Step 1: Initialize result list
        result = []  
        i = 0

        # Step 2: Loop through the string
        while i < len(s):
            # Step 3: Extract k characters
            chunk = s[i:i+k]

            # Step 4: Pad with fill if needed
            if len(chunk) < k:
                chunk += fill * (k - len(chunk))

            # Step 5: Add to result
            result.append(chunk)
            i += k

        # Step 6: Return final list
        return result