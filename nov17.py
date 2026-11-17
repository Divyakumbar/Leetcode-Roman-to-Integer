n=input("enter a value: ")
def is_palindrome(n):
    return n==n[::-1]
print(is_palindrome(n))