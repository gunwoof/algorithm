def hanoi(From,To,N) :
    global cnt
    if N == 1:
        print(From,To)
        return
    
    hanoi(From,6-From-To,N-1)
    print(From,To)
    hanoi(6-From-To,To,N-1)
    
number = int(input())
print(2**number-1) # 원반이 이동한 count
hanoi(1,3,number)
