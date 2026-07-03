class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) :return False
        dic1=Counter(s)
        dic2=Counter(t)
        return dic1==dic2