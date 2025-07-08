from math import *
a,b,c = 50,60,40
s = (a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))
area = sqrt(ar)
#area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle =",area)
