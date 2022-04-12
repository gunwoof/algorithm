def pack(number) :
    if number == 0 :
        return 1
    
    return number*pack(number-1)

number = int(input())
print(pack(number))