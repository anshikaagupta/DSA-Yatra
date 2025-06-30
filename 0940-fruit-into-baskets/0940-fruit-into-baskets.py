class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #bruteforce solution
        '''maxans=0
        
        for i in range(len(fruits)):
            setx=set()
            for j in range(i,len(fruits)):
                setx.add(fruits[j])
                if (len(setx)<=2):
                    maxans=max(maxans,j-i+1)
                else:
                    break
        return maxans'''

        left=0
        setx={}
        maxans=0
        for right in range(left,len(fruits)):
            fruitss=fruits[right]
            if fruitss in setx:
                setx[fruitss]+=1
            else:
                setx[fruitss]=1
            while len(setx)>2:
                fr_left=fruits[left]
                setx[fr_left]-=1
                if setx[fr_left]==0:
                    del setx[fr_left]
                left+=1
            maxans=max(maxans,right-left+1)
        return maxans


        