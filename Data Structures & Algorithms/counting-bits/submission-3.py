class Solution:
    def countBits(self, n: int) -> List[int]:
        rs=[]
        for i in range(n+1):
            res=0
            while i!=0:
                i&=i-1
                res+=1
            rs.append(res)
        return rs
        