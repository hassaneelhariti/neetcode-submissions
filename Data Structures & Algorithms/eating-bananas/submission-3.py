class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h: return max(piles)
        if sum(piles)<=h : return 1
        l,r=0,max(piles)-1
        res=max(piles)
        while l<=r:
            mid=(l+r)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/mid)
            if hours<=h: 
                res=mid
                r=mid-1
            else :
                l=mid+1
        return res
        

        


