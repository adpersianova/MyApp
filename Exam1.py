p = 4
a = 3
d = 2

D = p*p - 4*p*d
if D>0:
    x1 = (-a + D**(1/2))/(2*p)
    x2 = (-a - D**(1/2))/(2*p)
    print ("Первый корень ",round(x1), " второй корень ",round(x2))
elif D==0:
    x = (-b)/(2*a)
    print("корень: ",x)
else:
    print("нет корней")
