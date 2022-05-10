a=input("enter:-")
b=a.split()
print(b)
i=0
while i<len(b):
    j=0
    while j<len(b):
        if b[i][j]==0:
            c=b[i][j].upper
            print(c)
        j+=1
    i+=1
# print(c)