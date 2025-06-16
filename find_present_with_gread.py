print("Please enter 5 Subject Numbers")
a =int(input("enter first Subject number = "))
b =int(input("enter second Subject number = "))
c =int(input("enter third Subject number = "))
d =int(input("enter forth Subject number = "))
e =int(input("enter fifth Subject number = "))
pre = (a+b+c+d+e)/5
if pre<33:
    print(pre,"% Fail.")
elif pre>=33 and pre<45 :
    print(pre,"% Pass with 3rd Division.")
elif pre>=45 and pre<60 :
    print(pre,"% Pass with 2nd Division.")
else:
    print(pre,"% Pass with 1st Division.")