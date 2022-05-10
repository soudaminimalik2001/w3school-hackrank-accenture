n=int(input("enter number"))
if n%2!=0:
    print("weird")
elif n%2==0:
    if n>2 and n<5:
        print("not weird")
    elif n>6 and n<20:
        print("WEIRD")
    elif n>20:
        print("NOT WEIRD")