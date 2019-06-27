def maxIndex(ls):
    maxNum=0
    maxIndex=0
    for i in range(len(ls)):
        if int(ls[i])>maxNum:
            maxNum=ls[i]
            maxIndex=i
    return maxIndex
def optimalValueKnapsack(items,totalWeight,ValuePerWeight,ValueList,WeightList):
    optimalValue=0
    residualWeight=0
    while residualWeight!=totalWeight:
        totalWeight=totalWeight-residualWeight
        maxValuePerWIndex=maxIndex(ValuePerWeight)
        if WeightList[maxValuePerWIndex]<totalWeight:
            optimalValue=optimalValue+ValueList[maxValuePerWIndex]
        else:
            optimalValue=optimalValue+totalWeight*ValuePerWeight[maxValuePerWIndex]
            break
        residualWeight=residualWeight+WeightList[maxValuePerWIndex]
        ValuePerWeight.pop()
        ValueList.pop()
        WeightList.pop()
    return optimalValue

def __main__():
    InputValue = input("Enter the total items, total Weight of the KnapSack")
    n1, n2= InputValue.split()
    items, totalWeight=eval(n1), eval(n2)
    if totalWeight==0:
        return totalWeight
    else:
        CountOfItems=0
        ValueList=[]
        WeightList=[]
        ValuePerWeight=[]
        while CountOfItems<items:
            Values, weights= input("Enter the value and weights").split()
            if eval(Values)!=0:
                ValuePerWeight.append(eval(Values)/eval(weights))
                ValueList.append(eval(Values))
                WeightList.append(eval(weights))
            CountOfItems=CountOfItems+1
    print(optimalValueKnapsack(items,totalWeight,ValuePerWeight,ValueList,WeightList))
__main__()