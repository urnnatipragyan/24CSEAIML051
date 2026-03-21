paragraph = "Madam Arora teaches malayalam and level civic duties"
words = paragraph.lower().split()
word_count = len(words)
palindrome_count = 0
for word in words:
    if word == word[::-1]:
        palindrome_count += 1
print("Reversed words:")
for word in words:
    print(word[::-1])
print("\nTotal number of words:", word_count)
print("Number of palindrome words:", palindrome_count)
