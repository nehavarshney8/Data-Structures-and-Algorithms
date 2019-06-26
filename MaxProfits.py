def maxProfits(ls, lp):
    lsSorted=sorted(ls, reverse=True)
    lpSorted=sorted(lp, reverse=True)
    k=sum(list(map(lambda x,y:x*y, lsSorted, lpSorted)))
    return k

def __main__():
    slots=eval(input("Enter the number of slots: "))
    profitPerSlot=input("Enter the profit per slot in sequence: ").split()
    clicksPerSlot=input("Enter the number of clicks per slot in sequence: ").split()
    profitsList=[]
    clicksList=[]
    for element in profitPerSlot:
        profitsList.append(eval(element))
    for element in clicksPerSlot:
        clicksList.append(eval(element))
    print(maxProfits(profitsList, clicksList))
__main__()