from sys import stdin as s

def odd(x,y):
    print(x-y,end="")
    print("/",end="")
    print(1+y)

def even(x,y):
    print(1+y,end="")
    print("/",end="")
    print(x-y)
    

X=int(s.readline())
if X == 1:
    print("1/1")
    exit()

# X가 몇 번째 라인에 있는지 뽑아냄
i=2
while 1:
    if (i-1)*i//2 < X and X <= i*(i+1)//2: # 라인의 경계가 등차가 1인 등차수열의 합이다
        break
    i += 1

standard= X - (i-1)*i//2 - 1 # X가 라인의 몇 번째 수인지 체크


if i%2==0:
    even(i,standard)
else :
    odd(i,standard)