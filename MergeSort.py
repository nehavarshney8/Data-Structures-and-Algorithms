def Merge(ls, lp):
    d=[]
    l=len(ls)+len(lp)
    while len(d)!=l:
        if len(ls)==0:
            for elements in lp:
                d.append(elements)
        elif len(lp)==0:
            for elements in ls:
                d.append(elements)
        else:
            if ls[0]<lp[0]:
                d.append(ls[0])
                ls.pop(0)
            else:
                d.append(lp[0])
                lp.pop(0)
    return d
import math

def MG(ls):
    low=0
    high=len(ls)-1
    if len(ls)==1:
        return ls
    elif low<high:
        m=math.floor(len(ls)/2)
        mid=math.floor((low+high)/2)
        return Merge(MG(ls[low:mid+1]), MG(ls[mid+1:high+1]))
    
def __main__():
    numbers= input("Enter the numbers you would like to sort in sequence").split()
    FinalN=[]
    for elements in numbers:
        FinalN.append(eval(elements))
    print( MG(FinalN))
__main__()