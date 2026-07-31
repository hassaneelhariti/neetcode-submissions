class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            t=0
            while i!=0:
                t+=1
                i&=i-1
            res.append(t)
        return res
