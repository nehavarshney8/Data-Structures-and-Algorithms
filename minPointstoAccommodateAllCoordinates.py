def maxRepeats(ls):
    ds={}
    for i in range(len(ls)):
        if ls[i] in ds.keys():
            ds[ls[i]]+=1
        else:
            ds[ls[i]]=1
    maxValue=0
    for key, value in ds.items():
        if value>maxValue:
            maxValue=value
    for element in [key for key, value in ds.items() if value==maxValue]:
        return element


def minPoints(Sorted,TotalPoints):
    n=0
    check=[]
    commonC=[]
    #ramp=[]
    pl=0
    while n<TotalPoints:
        temp=Sorted[n]
        for k in range(temp[0], temp[1]+1):
            for i in range(n+1, len(Sorted)):
                for j in range(Sorted[i][0], Sorted[i][1]+1):
                    if j==k:
                        check.append(k)
    
        mostOccuring =maxRepeats(check)
        #print(mostOccuring)
        for p in range(n+1, len(Sorted)):
            ld=[i for i in range(Sorted[p][0], Sorted[p][1]) if i==mostOccuring]
        if mostOccuring==None:
            commonC.append(Sorted[0][0])
        else:
            commonC.append(mostOccuring)
        #print(commonC)
    
        n1=0
        po=[]
        while n1<len(Sorted):
            for i in range(Sorted[n1][0], Sorted[n1][1]+1):
                if i==mostOccuring:
                    po.append(Sorted[n1])
            n1=n1+1
        ko=[]
        for element in Sorted:
            if element not in po:
                ko.append(element)
        #print(ko)
        if len(ko)==1:
            commonC.append(ko[0][0])
            break
        elif len(ko)==0:
            break
        TotalPoints=len(ko)-1
        Sorted=ko[1:]
    
    #for c in list(set(commonC)):
        #print(c)
        
    tee=list(set(commonC))
    print (len(tee))
    for i in range (len(tee)):
        print(tee[i], end=' ')

def __main__():
    TotalPoints=eval(input("Enter the total number of Points"))
    n=0
    points=[]
    while n<TotalPoints:
        temp=[]
        Coordinates=input("Keep entering the coordinates").split()
        for elements in Coordinates:
            temp.append(eval(elements))
        points.append(temp)
        n=n+1
    Sorted=sorted(points)
    minPoints(Sorted,TotalPoints)
    
__main__()