def __main__():
    actual=eval(input("enter the sum value"))
    ls=[10,5,1]
    Inter=0
    coins=0
    for i in range(len(ls)):
        Inter=0
        if (actual//ls[i])>0:
            coins=coins+actual//ls[i]
            #This is really cool about GitHub, see if you can see the change in your folder
            # yeah bisha
            Inter=ls[i]*(actual//ls[i])
        actual=actual-Inter
    print(coins)
__main__()
