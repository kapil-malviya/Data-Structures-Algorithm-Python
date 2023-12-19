'''
num = int(input("enter : "))
fact = 1

for i in range (1, num + 1):
	fact = fact * i

print(fact)
'''

# -----------------------------
'''

num = int(input("enter : "))
fact = 1

i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print(fact)

'''
# -----------------------------

def fact(num):
    if num == 0 or num ==1:
        return 1
    return num * fact(num - 1)
        

print(fact(5))
