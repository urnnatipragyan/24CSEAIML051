d1 = {}
n = int(input("how many items:"))
for i in range(n):
    k = input("enter key:")
    v = input("enter value:")
    d1[k] = v
d2 = {}
for k in d1:
    d2[d1[k]] = k
print("first dictionary:")
print(d1)
print("second dictionary(values as keys):")
print(d2)