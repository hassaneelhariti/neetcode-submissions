class Solution:
        def isValid(self, s: str) -> bool:
                if len(s) <= 1:
                        return False

                dic = {"(": ")", "{": "}", "[": "]"}
                stk = []

                for i in s:
                        if i in dic:
                                stk.append(i)
                                continue

                        if stk:
                                if i != dic[stk.pop()]:
                                        return False
                        else:
                                return False

                return len(stk) == 0
