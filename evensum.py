T=int(input())
for i in range(T):
    a,b=map(int, input().split())
    a_even=a//2
    a_odd=a-a_even
    b_even=b//2
    b_odd=b-b_even
    ans=(a_even*b_even)+(a_odd*b_odd)
    print(ans)

