# a=int(input("enter number"))
# i=0
# sum=0
# while i<a:
#     b=i%4
#     sum+=b
#     i+=1
# print(sum)

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
numbers=[2,3,6,5]
max1=0
max2=0
i=0
while i<len(numbers):
    if numbers[i]>max1:
        max2=max1
        max1=numbers[i]
    
    elif numbers[i]>max2:
        max2=numbers[i]
    # elif numbers[i]
    i+=1
print(max2)