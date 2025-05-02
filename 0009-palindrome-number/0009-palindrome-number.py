class Solution:
    def isPalindrome(self, x: int,i=0) -> bool:
        s=str(x)
        l=len(s)
        if i == l//2:
            return True
        if s[i]!=s[l-i-1]:
            return False
        return self.isPalindrome(x,i+1)
        