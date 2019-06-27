def numberOfPitStops(d,tankFullM,numberofStops,stopList):
    distanceCovered=0
    i=0
    pitstop=0
    while distanceCovered<d:
        while i<=len(stopList):
            if abs(distanceCovered-stopList[i])<=tankFullM:
                if i==len(stopList)-1:
                    distanceCovered=stopList[i]
                    break
                i=i+1
                continue
            else:
                if stopList[i]-stopList[i-1]<=tankFullM:
                    pitstop=pitstop+1
                    distanceCovered=stopList[i-1]
                else:
                    #print("Trip Cannot happen")
                    pitstop=-1
                    distanceCovered=d
                    break
        i=i-1
    return pitstop

def __main__():
    d=eval(input("Enter the total distance between the points"))
    tankFullM= eval(input("Enter the full tank Mileage"))
    s=eval(input("Enter the number of stops between the points"))
    stops=input("Enter the pitstop distances from the starting point").split()
    stopList=[]
    for elements in stops:
        stopList.append(eval(elements))
    stopList.append(d)
    print(numberOfPitStops(d,tankFullM,s,stopList))
    
__main__()