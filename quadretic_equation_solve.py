from math import*
a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
d = b**2 - 4*a*c
if d == 0:
    root = b/2*a
    print("one real root :",root)
elif d>0 :
    root1 = (-b-sqrt(d))/(2*a)
    root2 = (-b+sqrt(d))/(2*a)
    print("two real roots :",root1,"And",root2)
elif d<0:
    real_part =-b/(2*a)
    imes_part =(sqrt(-d)/(2*a))
    print(f"two Complex roots :{real_part}+{imes_part}i and {real_part}-{imes_part}i")
    #print(f"Two complex roots: {real_part}+{imas_part}i and {real_part}-{imas_part}i")


