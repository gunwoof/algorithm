number = []
for i in range(9) :
    number.append(int(input()))

mnumber=max(number)
print(mnumber)
print(number.index(mnumber)+1)

