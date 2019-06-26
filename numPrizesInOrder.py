def __main__():
    n=eval(input("Enter the number"))
    x=1
    num=0
    Summed=0
    while Summed<=n:
        Summed=((x+1)*(x+2))/2
        num=x-1
        x=x+1
    num
    pd=[]
    for i in range(1, num+1):
        pd.append(i)
    sumOf=sum(pd)
    pd.append(n-sumOf)
    print(len(pd))
    for elements in pd:
        print(elements, end=' ')
__main__()