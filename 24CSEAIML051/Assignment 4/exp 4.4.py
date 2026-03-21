a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


gcd_ab = gcd(a, b)
gcd_abc = gcd(gcd_ab, c)

print("GCD of", a, b, c, "is:", gcd_abc)
