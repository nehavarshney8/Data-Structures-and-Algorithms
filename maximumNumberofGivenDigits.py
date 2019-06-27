def Digits(n):
    D=[]
    while n!=0:
        D.append(n%10)
        n=n//10
    D.reverse()
    return D  

def NumDigits(n):
    D=0
    if n==0:
        return 1
    else:
        
        while n>0:
            D+=1
            n=n//10
    return D

def EpicN(a, b):
    maxN=0
    NumDigitsA=NumDigits(a)
    NumDigitsB=NumDigits(b)
    if NumDigitsA==NumDigitsB:
        if a>b:
            maxN=a
        else:
            maxN=b
    elif a==0 or b==0:
        if a>b:
            maxN=a
        else:
            maxN=b
    else:
        if NumDigitsA>NumDigitsB:
            a,b=b,a
        DA=Digits(a)
        DB=Digits(b)
        check=[]
        for i in range(len(DA)):
            if DB[i]==DA[i]:
                check.append(1)
        if len(check)==len(DA):
            if DB[0]>DB[len(DB)-1]:
                maxN=a
            else:
                maxN=b
        else:
            for i in range(len(DA)):
                if DB[i]==DA[i]: 
                    continue
                elif DB[i]>DA[i]:
                    maxN=b
                elif DB[i]<DA[i]:
                    maxN=a
    return maxN
def __main__():
    totalN= eval(input("Enter the total number of numbers"))
    ls=[]
    numbers=input("Keep entering the numbers").split()
    for elements in numbers:
        ls.append(eval(elements))

    isTrue=True
    F=[]
    while isTrue:
        maxP=0
        for i in range(len(ls)):
            k=EpicN(maxP,ls[i])
            #print(k)
            maxP=k
        F.append(maxP)
        ls.remove(maxP)
        if len(ls)>0:
            isTrue=True
        else:
            isTrue=False
    s=eval("".join(map(str, F)))
    print(s)
__main__()