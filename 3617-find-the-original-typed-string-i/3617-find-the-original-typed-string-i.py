class Solution:
    def possibleStringCount(self, word: str) -> int:
        # Step 1: Start with 1 possible original (no mistake)
        ans = 1

        # Step 2: Loop from the second character
        for i in range(1, len(word)):
            # Step 3: If current and previous characters are the same
            if word[i] == word[i - 1]:
                ans += 1  # Step 4: Count as a possible duplication

        # Step 5: Return total count
        return ans