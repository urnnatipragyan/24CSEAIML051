total = 0
count = 1


while count <= 3:
    num = int(input(f"Enter positive integer {count}: "))
    if num > 0:
        total += num
        count += 1
    else:
        print("Please enter a positive integer!")

print("Sum of the 3 positive integers is:", total)
