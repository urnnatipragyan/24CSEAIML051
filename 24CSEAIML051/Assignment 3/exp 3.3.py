a = float(input("Enter first value a: "))
b = float(input("Enter second value b: "))
c = float(input("Enter third value c: "))

d = b*b - 4*a*c

if d > 0:
    r1 = (-b + d**0.5)/ (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print("Real roots are:", r1, "and", r2)
elif d == 0:
    r = -b / (2*a)
    print("Real root is:", r)
else:
    print("No real roots")
