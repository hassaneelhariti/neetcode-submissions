class Solution:
    def climbStairs(self, n: int) -> int:
        dp1=1
        dp2=1
        while n>0:
            tmp=dp1
            dp1=dp1+dp2
            dp2=tmp
            n-=1
        return dp2
