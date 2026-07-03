class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=1
        m=1
        zero=0
        List=[]
        for i in nums:
            if i !=0:
                m=m*i
            elif i==0:
                zero+=1
            n=n*i
        for i in nums:
            if i==0 and zero==1:
                List.append(m)
            elif i==0 and zero>1:
                List.append(0)
            else:
                List.append(int(n/i))
        return List

        