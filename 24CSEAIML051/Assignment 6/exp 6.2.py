fruits = ["apple","banana","mango","grapes"]
rev_list = []
print("fruits from last to first with length:")
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i], "length:", len(fruits[i]))
for f in fruits:
    rev_list.append(f[::-1])
print("list of reversed elements:")
print(rev_list)