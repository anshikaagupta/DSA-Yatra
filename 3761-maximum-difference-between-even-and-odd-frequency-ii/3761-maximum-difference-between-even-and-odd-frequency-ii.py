class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        inf = float('inf')
        def solve(a, b):
            ca, cb = 0, 0
            res = -inf
            oo, oe, eo, ee = [], [], [], [(-1, 0, 0, 0)] # (idx, ca, cb, min(ca-cb) before idx)
            
            def find(pref_arr, cur_idx, ca, cb):
                if ca == 0 or cb == 0:
                    return inf
                
                t_idx = cur_idx - k
                if t_idx < -1:
                    return inf
                if pref_arr[0][0] > t_idx or pref_arr[0][1] >= ca or pref_arr[0][2] >= cb:
                    return inf
                l, r = 0, len(pref_arr)-1
                while l < r:
                    m = (l+r+1) // 2
                    if pref_arr[m][0] <= t_idx and pref_arr[m][1] < ca and pref_arr[m][2] < cb:
                        l = m
                    else:
                        r = m-1
                # print(f"found l={l}")
                return pref_arr[l][3]
            
            def update(i, ca, cb, prev):
                if not prev:
                    prev.append((i, ca, cb, ca-cb))
                else:
                    prev.append((i, ca, cb, min(ca-cb, prev[-1][3])))
                    
            n = len(s)
            pref_cnta = [0] * n
            pref_cntb = [0] * n
            for i, c in enumerate(s):
                if c == a:
                    ca += 1
                if c == b:
                    cb += 1
                if ca % 2 == 1 and cb % 2 == 0 and ee:
                    res = max(res, ca - cb - find(ee, i, ca, cb))
                if ca % 2 == 1 and cb % 2 == 1 and eo:
                    res = max(res, ca - cb - find(eo, i, ca, cb))
                if ca % 2 == 0 and cb % 2 == 0 and oe:
                    res = max(res, ca - cb - find(oe, i, ca, cb))
                if ca % 2 == 0 and cb % 2 == 1 and oo:
                    res = max(res, ca - cb - find(oo, i, ca, cb))
                
                # print(f"i={i}, c={c}, res={res}, ca={ca} cb={cb}, ee={ee}")
                
                if ca % 2 == 1 and cb % 2 == 0:
                    update(i, ca, cb, oe)
                if ca % 2 == 1 and cb % 2 == 1:
                    update(i, ca, cb, oo)
                if ca % 2 == 0 and cb % 2 == 0:
                    update(i, ca, cb, ee)
                if ca % 2 == 0 and cb % 2 == 1:
                    update(i, ca, cb, eo)
            return res
                        
        
        chars = '01234'
        res = -inf
        # res = solve('1', '3')
        for a in chars:
            for b in chars:
                if a != b:
                    # print(a, b, solve(a, b))
                    res = max(res, solve(a, b))
        return res
