import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),  
        }


        stack=[]

        for i in range(len(tokens)):
            
            if tokens[i] in oops: 
                b = stack.pop()
                a = stack.pop()
                stack.append(oops[tokens[i]](a,b))
            else : 
                stack.append(int(tokens[i]))
                
        return stack[-1]

       
        