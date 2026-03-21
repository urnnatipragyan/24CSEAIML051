sentence = input("enter a sentence:")
list1 = sentence.split()
print("elements of list1 with index:")
for index,word in enumerate(list1):
    print(index,word)
list2 = list(range(1,len(list1)+1))
list3 = list(zip(list1,list2))
print("combined list using zip:")
print(list3)