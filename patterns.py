
print("a)")
print()
for i in range(1,11):
    for j in range(i):
        print("*",end=" ")
    print()

print("b)")
print()
for i in range (9,-1,-1):
    for j in range (i+1):
        print("*",end=" ")
    print()
    
print("c)")
print()

for i in range(11 - 1):
    # print spaces
    for j in range(i + 1):
        print(' ', end=' ')
    # print stars
    for k in range(11 - i - 1):
        print('*', end=' ')
    print()
    
print("d)")
print()

for i in range(11):
    for j in range(1, 11 - i):
        print(" ", end=" ")
    for k in range(0, i + 1):
        print("*", end=" ")
    print()