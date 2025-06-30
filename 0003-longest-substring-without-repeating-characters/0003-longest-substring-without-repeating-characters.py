class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        if len(s)==0:
            return 0
        maxset=float('-inf')
        setx=set()
        for r in range(len(s)):
            if s[r] in setx:
                while l<r and s[r] in setx:
                    setx.remove(s[l])
                    l+=1
            setx.add(s[r])
            maxset=max(maxset,r-l+1)
        return maxset
        