class Solution:
    def muchbit(self,n):
        rs=0
        while n!=0:
            n&=(n-1)
            rs+=1
        return rs
    def countBits(self, n: int) -> List[int]:
        rs=[]
        for i in range(n+1):
            rs.append(self.muchbit(i))
        return rs
        