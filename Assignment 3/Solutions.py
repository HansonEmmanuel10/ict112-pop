Question 1
original_string = "Programming"
reversed_string = original_string[::-1]
print(reversed_string)


Question 2
full_name = input("Enter your full name: ")
initials = ''.join([name[0].upper() + '.' for name in full_name.split()])
print(initials)


QUESTION 3
def is_palindrome(s):
    return s == s[::-1]
  
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
  
Question 4

sentence = input("Enter a sentence: ")
words = sentence.split()

num_words = len(words)

print(f"The sentence '{sentence}' has {num_words} words.")


Question 5

original_string = "This is a string and it is an example."

# Replace "is" with "was"
modified_string = original_string.replace("is", "was")

print(modified_string)

