class Solution:
    def reverse(self, x: int) -> int:
        m = True
        if x < 0:
            m = False 
            x = x*-1
        sum1 = 0 
        for i in range(len(str(x))):
            sum1 += (10**(len(str(x))-1-i))*(int(str(x)[-i-1]))
        if sum1 < (2**31) -1  and sum1 > -2**31 : 
            if m is False:
                return sum1*-1
            else:
                return sum1 
        else:
            return 0 
                           
                        
       
        