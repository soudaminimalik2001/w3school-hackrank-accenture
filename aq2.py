def differenceofSum():
    n=int(input())
    m=int(input())
    i=0
    Sum=0
    Sum1=0
    while i<=(m):
        if i%n==0:
            Sum=Sum+i
        else:
            Sum1=Sum1+i
        i=i+1
    return Sum1-Sum
print(differenceofSum())