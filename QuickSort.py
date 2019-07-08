def Partition(ls, l, r):
    x=ls[l]
    j=l;
    
    for i in range(l+1, r+1):
        if x>= ls[i]:
            j=j+1
            ls[i], ls[j]=ls[j], ls[i]
    ls[l], ls[j]=ls[j], ls[l]
    return j

import random
import math
def QuickSort(ls, l, r):
    if l>=r:
        return
    k = random.randint(l, r)
    ls[l], ls[k] = ls[k], ls[l]
    m=Partition(ls, l, r)
    QuickSort(ls, l, m-1)
    QuickSort(ls, m+1, r)

    
def __main__():
    temp=[]
    N= input("Enter the total number of elements in the list")
    Num = input("Enter the numbers in sequence").split()
    for elements in Num:
        temp.append(eval(elements))
    QuickSort(temp, 0, len(temp)-1)
    for elements in temp:
        print(elements, end=' ')

__main__()