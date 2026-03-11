'''
write a function that replaces all spaces in a string with underscores
'''
def replace_spaces(s):
    lst = list(s)

    for i in range(len(lst)):
        if lst[i] == " ":
            lst[i] = "_"

    result = "".join(lst)
    return result

s = " a b d b "
print(replace_spaces(s))

# STATUS: all good