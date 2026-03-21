text = input("Enter a string: ")
clean_text = text.replace(" ", "").lower()

if clean_text == clean_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
