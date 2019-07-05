import math
def bs(ls, key, low, high):
    if low==high and ls[low]==key:
        return low
    elif low==high and ls[low]!=key:
        return -1
    elif high<low:
        return -1
    else:
        mid=math.floor((low+high)/2)
        if key==ls[mid]:
            return mid
        elif key>ls[mid]:
            low=mid+1
            return bs(ls, key, low, high)
        elif key<ls[mid]:
            high=mid-1
            return bs(ls, key, low, high) 
def __main__():
    import math
    totalElements=input("Enter the total number of elements followed by elements in sequence").split()
    ele=totalElements[1:]
    seq=[]
    for elements in ele:
        seq.append(eval(elements))
    searchEle=input("Enter the total search elements and elements in order").split()
    elem=searchEle[1:]
    searchSeq=[]
    for elements in elem:
        searchSeq.append(eval(elements))
    f=[]
    for element in searchSeq:
        f.append(bs(seq, element, 0, len(seq)-1))
    for element in f:
        print(element, end=' ')
__main__()