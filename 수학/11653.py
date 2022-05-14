from sys import stdin as s

number = int(s.readline())
small_number=[]


if number == 1:
    exit()
elif number == 2:
    small_number.append(2)
elif number == 3:
    small_number.append(3)
else:
    for i in range(2,number+1):
        while number%i ==0:
            small_number.append(i)
            number = number//i

for i in small_number:
    print(i)
