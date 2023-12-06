# Combination of number in a string

def combinations(string, prefix='', index=0):
    if index == len(string):
        if prefix != '':
            print(prefix)
        return

    combinations(string, prefix + string[index], index + 1)

    combinations(string, prefix, index + 1)


string = input("enter no :")

combinations(string)

# x = combinations(string)

# print(x)
