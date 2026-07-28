class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)-1
        s1=sorted(s1)
        while r<len(s2):
            dic2=sorted(s2[l:r+1])
            if s1==dic2:
                return True
            l+=1
            r+=1
        return False
