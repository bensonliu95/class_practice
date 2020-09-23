for x in range(1,10):
    s=""
    for y in range(1,x+1):
        a=x*y
        s=s+str(y)+"x"+str(x)+"="+str(a)+" "
    print(s)