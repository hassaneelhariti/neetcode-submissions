class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic={}
        tdic={}
        for i in s:
            sdic[i]= sdic.get(i,0)+1

        for i in t:
            tdic[i]= tdic.get(i,0)+1
        
        return sdic==tdic