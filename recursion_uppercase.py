# Count the no of uppercases

def uppercase(string, index=0):

    if index == len(string):
        return 0
    
    if string[index].isupper():
        return 1 + uppercase(string, index + 1)
    else:
        return uppercase(string, index + 1)


string = 'abc V df X g S S xXX'
uppercase_count = uppercase(string)

print(uppercase_count)