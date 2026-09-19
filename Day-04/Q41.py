#Check whether a number is a palindrome.
def is_palindrome(n):
    # Convert the number to a string
    s = str(n)
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False