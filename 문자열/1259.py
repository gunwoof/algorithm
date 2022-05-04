from sys import stdin as s

while 1 :
    numbers=s.readline().rstrip()
    if numbers == "0":
        exit()
    if numbers == numbers[::-1]:
        print("yes")
    else :
        print("no")

    