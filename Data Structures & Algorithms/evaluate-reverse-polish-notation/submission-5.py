class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        stk=[]
        for i in tokens:
            if i=="+":
                #
                b = stk.pop()   
                a = stk.pop()
                res=a+b
                stk.append(res)  
            elif i=="*":
                #
                b = stk.pop()   
                a = stk.pop()
                res=a*b
                stk.append(res) 
                
            elif i=="-":
                #
                b = stk.pop()   
                a = stk.pop()
                res=a-b
                stk.append(res) 
            elif i=="/":
                #
                b = stk.pop()   
                a = stk.pop()
                stk.append(int(a/b)) 
            else:
                stk.append(int(i))
        print(int(-11))
        return int(stk.pop())