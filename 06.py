'''
write a recursive function that takes a list of numbers and returns a list 
containing all possible permutations (orderings) of those numbers
'''
def permutations(nums):
    if len(nums) == 1:
        return [nums]
    
    result = []

    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i] + nums[i+1:]

        perms = permutations(remaining)

        for p in perms:
            result.append([current] + p)
    
    return result

# STATUS: all good4