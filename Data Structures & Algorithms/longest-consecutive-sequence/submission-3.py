class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        t=list(set(nums))
        t.sort()
        
        k=[1]*len(t)
        j=0
        for i in range(len(t)-1):
            if t[i]+1==t[i+1]:
                k[j]=k[j]+1
            else:
                j+=1
        if len(nums)==0:
            longuest=0
        else: 
            longuest=max(k)
        return longuest
        