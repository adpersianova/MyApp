p = 4
a = 3
d = 2
D = p*p - 4*p*d
if D>0:
    x1 = (-a + D**(1/2))/(2*p)
    x2 = (-a - D**(1/2))/(2*p)
    print ("the first root ",round(x1), " the second root ",round(x2))
elif D==0:
    x = (-a)/(2*p)
    print("root: ",x)
else:
    print("no roots")
