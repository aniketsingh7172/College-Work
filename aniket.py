def a_sqrt(n):
    if n>=0:
        v=n**(1/2)
        return v
    else:
        e=f"value error:({n}) Please enter positive value"
        return e
def a_qrt(n):
    if n>=0:
        v=n**(1/3)
        return v
    else:
        e=f"value error:({n}) Please enter positive value"
        return e



# import math as s
# a=s.sqrt(9)
# b=s.isqrt(-8)
# print(b)