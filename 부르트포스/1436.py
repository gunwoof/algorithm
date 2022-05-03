# 처음에는 666이 4개가 될때 '좌'를 더하지 '우'를 더하는지를 고민했다.(쓰래기 고민)
# 브루트포스의 이름에 맞게 0부터 모두 "666"이 나올때만 체크하면 된다(정답)

n = int(input())
count =0 # 종말의 숫자일때 count가 올라감
i=0 # 모든 숫자

while 1 :

    if '666' in str(i) :
        count +=1
        if count == n :
            print(i)
            break
    i += 1

