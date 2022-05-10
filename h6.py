def leap(year):
    if year%4==0:
        return "true"
    else:
        return "false"
year=int(input("enter year"))
print(leap(year))