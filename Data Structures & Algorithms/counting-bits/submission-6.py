class Solution:
    def countBits(self, n: int) -> List[int]:
        rs=[0]*(n+1)
        for i in range(n+1):
            rs[i]=self.fun(i)
        return rs
    def fun(self,n:int):
        ans=0
        while n!=0:
            ans+=1
            n&=n-1
        return ans