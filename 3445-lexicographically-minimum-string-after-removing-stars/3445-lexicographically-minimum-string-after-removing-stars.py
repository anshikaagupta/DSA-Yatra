class Solution:
    def clearStars(self, s: str) -> str:
        a,h = [*s],[]
        for i,c in enumerate(s):
            if c=='*': a[i] = a[-heappop(h)[1]] = ''
            else: heappush(h,(c,-i))
                
        return ''.join(a)