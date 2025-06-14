class Solution:
    def minMaxDifference(self, num: int) -> int:

        mxNum = mnNum = str(num)

        for ch in mxNum:
            if ch != '9': 
                mxNum = mxNum.replace(ch, '9')
                break

        for ch in mnNum:
            if ch != '0': 
                mnNum = mnNum.replace(ch, '0')
                break

        return int(mxNum) - int(mnNum)      