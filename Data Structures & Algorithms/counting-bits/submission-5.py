class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for j in range(n+1):
            ans=0
            i=j
            while i!=0:
                i&=i-1
                ans+=1
            res.append(ans)
        return res