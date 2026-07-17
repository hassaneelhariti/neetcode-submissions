class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h: return max(piles)
        k=0
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=0
            i=(l+r)//2
            for p in piles:
                k=k+math.ceil(p/i) 
            print(k)
            if k<=h: 
                res=min(res,i)
                r=i-1
            else:
                l=i+1
        return res
                
                