class Solution:

    def encode(self, strs: List[str]) -> str:
        single=""
        for s in strs :

            single += str(len(s)) + '#' + s
        return single
    def decode(self, s: str) -> List[str]:
        List=[]
        i=0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
                length=int(s[i:j])
            List.append(s[j+1:j+1+length])
            i=length+1+j
        return List
