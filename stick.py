T=int(input())
for i in range(T):
    list=int(input())
    list= map(int, input().split(' '))
    list2=set(list)
    if 0 in list2:
        print(len(list2)-1)
    else:
        print(len(list2))
