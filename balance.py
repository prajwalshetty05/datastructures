openlist=["[","{","("]
closelist=["]","}",")"]
def check(mystr):
        stack=[]
        for i in mystr:
            if i in openlist:
                stack.append(i)
            elif i in closelist:
                pos=closelist.index(i)
                if(len(stack)>0 and openlist[pos]==stack[len(stack)-1]):
                    stack.pop()
                else:
                    return "unbalanced"
        if(len(stack)==0):
            return "balanced"
        else:
            return "unbalanced"
string="{[({})]}"
print(check(string))
string="{([)]}})]"
print(check(string))
             
             
                    
        