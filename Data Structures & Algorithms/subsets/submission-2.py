class Solution:
    def fun(self,res: List[int],i:int):
        rs=[]
        for l in res:
            rs.append(l+[i])
            rs.append(l)
        return rs
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for i in nums:
            res=self.fun(res,i)
        return res