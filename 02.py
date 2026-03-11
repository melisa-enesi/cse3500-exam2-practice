'''
write a function that takes a non-empty string and returns True
if the string is a palindrome, otherwise return False
'''

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True

# STATUS: all good