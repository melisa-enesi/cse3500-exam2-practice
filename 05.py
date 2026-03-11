'''
write a recursive function that takes a non-negative integer n and returns 
the nth Fibonacci number, where each number is the sum of the two previous
numbers and the sequence starts with 0 and 1
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4)) #3

# STATUS: all good