'''
write a recursive function that takes a positive integer n and returns
the sum of all integers from 1 to n
'''
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n-1)

print(sum_to_n(5)) #15

# STATUS: all good