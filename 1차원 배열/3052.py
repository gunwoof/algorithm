number = []

for i in range(10) :
    a = int(input())
    b = a%42
    if b not in number :
        number.append(b)

print(len(number))