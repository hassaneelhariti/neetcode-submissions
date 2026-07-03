class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i)) + "@" + i

        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            a=0
            while s[j] !="@":
                j+=1
            a=int(s[i:j])
            res.append(s[j+1:j+a+1])
            i=j+a+1
        return res
        