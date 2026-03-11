'''
write a recursive function that takes a nested list of integers and returns
the product sum, where each nested list's sum is multiplied by its depth level
'''
def product_sum(array, depth=1):
    total = 0

    for element in array:
        if isinstance(element, list):
            total += product_sum(element, depth + 1)
        else:
            total += element
    
    return total * depth 

# STATUS: all good