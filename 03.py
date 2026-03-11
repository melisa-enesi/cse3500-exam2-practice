'''
write a recursive function that takes a non-negative 
integer n and returns the factorial of n, where 
n! = n * (n-1) * (n-2) * ... * 1 and 0! = 1
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5)) #120

# STATUS: all good