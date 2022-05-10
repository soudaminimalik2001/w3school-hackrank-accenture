input1=input()
input2=input()
def Anagrams():
    com=''
    i = 0
    while i <len(input1):
        if input1[i] in input2:
            com+=input1[i]
        i+=1
    if com==input1:
        return "YES"
    else:
        return "NO"
print(Anagrams())