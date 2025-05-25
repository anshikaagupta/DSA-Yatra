class Solution:
    def longestPalindrome(self, a: List[str]) -> int:
        z = Counter(a)
        return (sum((min(z[s],z[s[::-1]]),z[s]//2*2)[s[0]==s[1]] for s in z)
            +any(f&1 for s,f in z.items() if s[0]==s[1]))*2     