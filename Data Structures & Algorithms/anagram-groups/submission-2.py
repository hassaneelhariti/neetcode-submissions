class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            c = frozenset(Counter(i).items())
            if c not in dic:
                dic[c] = []
            dic[c].append(i)
        
        return list(dic.values())
