number = int(input())

if number%400 == 0 :
    print("1")
elif number%100 != 0 and number%4 == 0 :
    print("1")
else :
    print("0")