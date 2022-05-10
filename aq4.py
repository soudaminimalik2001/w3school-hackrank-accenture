p=int(input("enter"))
n=[]
x=0
while x<p:
    b=int(input("enter"))
    n.append(b)
    x=x+1
# n=[2,3,6,6,5]
print(n)
a=[]
j=0
while j<len(n):
    if n[j] not in a:
        a.append(n[j])
    j=j+1
print(a)
maximum=0
secondmaximum=0
i=0
while i<len(a):
    if a[i]>maximum:
        secondmaximum=maximum
        maximum=a[i]
    elif a[i]>secondmaximum:
        secondmaximum=a[i]
    i+=1
# print(maximum)
print(secondmaximum)